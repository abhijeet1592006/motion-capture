# Real-Time Human Pose Tracking with 2D Robot Visualization

I'm **Abhijeet Singh**, and this project is one of my many experiments combining **MediaPipe**, **Flask**, **OpenCV**, and **HTML/CSS/JS** to track a human body in real-time and animate a robot model based on joint angles.

---

## 📽️ Demo

![DEMO](https://github.com/abhijeet1592006/motion-capture/blob/main/demo.gif)

---

## 💡 What It Does

- Tracks real-time **human pose** using your webcam via MediaPipe
- Calculates **shoulder** and **elbow** angles of both arms
- Sends data through a **Flask API**
- Animates a **robot model** using **JavaScript transforms** based on live angles


---

## 🧠 Technologies Used

- 🔵 Python + Flask
- 🦾 OpenCV + MediaPipe
- 🎨 HTML + CSS + JS (Vanilla Gang Rise Up!)
- 🔁 REST API with `fetch()`
- 🧠 Math with `atan2()` for angles

---

## 🚀 How To Run It Locally

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/pose-tracker-bot.git

cd motion-capture
```
### 2. Install the Python dependencies

```bash
pip install flask opencv-python mediapipe flask-cors
```
### 3. Plug in a webcam
Make sure your camera is accessible and change cv2.VideoCapture(0) if needed (try 1 if it doesn’t work).

### 4. Run the Python backend
```bash

python app.py

```
### 5. Open the HTML file
**Just open index.html in your browser. The JS will hit the Flask API and animate the robot automatically**


# 🛡️ License & Credit
**This project is licensed under the MIT License — so feel free to use it, remix it, learn from it.**

**But,if you repost or use it in a video, just tag or credit:**

📸 @codebitbybit
👨‍💻 GitHub: abhijeet1592006

## 🙌 A Message From Me
**I'm just a student out here building cool stufs and leveling up daily. If this helped, drop a comment, follow on IG, or just fork it and make it better.**

### Peace out 
### — Abhijeet singh
