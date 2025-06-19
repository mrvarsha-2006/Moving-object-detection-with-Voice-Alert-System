import cv2
import time
import imutils
import threading
import pyttsx3
import queue
import os

# Initialize camera
cam = cv2.VideoCapture(0)
time.sleep(1)

if not cam.isOpened():
    print("[ERROR] Camera could not be opened.")
    exit()

# Voice engine setup (thread-safe)
engine = pyttsx3.init()
speak_queue = queue.Queue()

def speak_loop():
    while True:
        text = speak_queue.get()
        engine.say(text)
        engine.runAndWait()
        speak_queue.task_done()

# Start the background speaker thread
threading.Thread(target=speak_loop, daemon=True).start()

def speak_alert():
    if speak_queue.empty():  # Avoid spamming queue
        speak_queue.put("Motion detected")

# Folder to save images
save_path = "detected_frames"
os.makedirs(save_path, exist_ok=True)

# Motion detection variables
firstFrame = None
area = 500  # Minimum area to qualify as motion

while True:
    ret, img = cam.read()
    if not ret:
        print("[ERROR] Failed to read from camera.")
        break

    text = "Normal"
    img = imutils.resize(img, width=500)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)

    if firstFrame is None:
        firstFrame = gaussianImg
        continue

    imgDiff = cv2.absdiff(firstFrame, gaussianImg)
    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]
    threshImg = cv2.dilate(threshImg, None, iterations=2)

    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        if cv2.contourArea(c) < area:
            continue

        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Moving Object Detected"

        # 🔔 Trigger safe speaking alert
        speak_alert()

        # 💾 Save frame in custom folder
        timestamp_str = time.strftime('%Y%m%d_%H%M%S')
        filename = os.path.join(save_path, f"motion_{timestamp_str}.jpg")
        cv2.imwrite(filename, img)
        print(f"[INFO] Saved frame as: {filename}")

        break  # Avoid multiple alerts per frame

    # ⏱ Timestamp Overlay
    timestamp_disp = time.strftime("%Y-%m-%d %H:%M:%S")
    cv2.putText(img, f"Status: {text}", (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(img, timestamp_disp, (780, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow("Motion Detection", img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
