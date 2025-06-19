# 🕵️‍♀️ Moving Object Detection with Voice Alert System

Greetings everyone! This project is a real-time motion detection system using **OpenCV**, **Python**, and **pyttsx3**. It captures movement through your webcam, announces "Motion Detected" using voice alerts, and saves snapshots of detected motion for evidence or logging.

This system can be used in:
- 🏠 Home security
- 🏢 Office/ Bank/ Hospital surveillance
- 🧪 Smart automation experiments

---

## 📌 Features

🧠 **Real-time Motion Detection**  
🎙️ **Voice Alerts** using `pyttsx3` (non-blocking thread-safe implementation)  
📸 **Automatic Frame Capture** on motion  
🗂️ **Organised Saving** of motion frames with timestamps  
📅 **Time Overlay** on live feed  
📐 **Contour-based Filtering** to ignore small movements  
🖥️ **Live Video Feed** using OpenCV

---

## 🧰 Tech Stack

### 💻 Software
- Python 3.x
- OpenCV
- imutils
- pyttsx3
- threading and queue (standard Python modules)

### 🧠 Libraries Used
```bash
pip install opencv-python imutils pyttsx3
```

---

## 🛠️ How to Run

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/mrvarsha-2006/Moving-object-detection-with-Voice-Alert-System/blob/main/moving_object.py
cd motion-detection-system
```

### 2️⃣ Run the Script
```bash
python moving_object.py
```

> The webcam will open. When motion is detected, the system will:
> - Announce via voice: “Motion detected”
> - Draw a bounding box around the movement
> - Save the frame inside the `detected_frames` folder

### 3️⃣ Stop
Press **`q`** to quit the program gracefully.

---

## 🔍 How It Works

1. Captures live video from the default webcam.
2. Applies grayscale and Gaussian blur for noise reduction.
3. Compares the current frame with the first static frame.
4. If a difference (motion) is detected above a threshold area:
   - Highlights motion region using a green rectangle.
   - Announces motion through a background voice thread.
   - Saves the frame as `motion_YYYYMMDD_HHMMSS.jpg` in the `detected_frames` folder.

---

## 🧪 Results

| Feature | Output |
|--------|--------|
| Motion Detection | ✅ Accurate in real-time |
| Frame Saving | ✅ Saved with timestamp |
| Voice Alert | ✅ Clear and timely |
| CPU Usage | 🟢 Low due to threading |
| Extensibility | 🔁 Easy to enhance (email alerts, cloud sync, etc.) |

---

## 🚀 Future Improvements

- Add **email/SMS alerts** using SMTP or Twilio  
- Integrate with **cloud storage** (Google Drive/Dropbox)  
- Use **YOLO or object detection** for filtering specific targets  
- Add **face recognition** to distinguish known/unknown persons  
- Make it work on **Raspberry Pi** for portable deployment

---

## 👩‍💻 Author

This project is done by **Varsha M R**  
Pre-Final Year Biomedical Engineering Student  

---

## 🔗 GitHub Repository

👉 https://github.com/mrvarsha-2006/Moving-object-detection-with-Voice-Alert-System
