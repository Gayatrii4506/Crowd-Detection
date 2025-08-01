
# 👥 Crowd Detection using OpenCV

A Python-based real-time crowd detection system using computer vision techniques like contour detection and motion analysis. This tool is useful for public space monitoring, crowd control, and smart surveillance.

---

## 🚀 Features

- 📸 Real-time video input via webcam or video file
- 🔍 Crowd size estimation using contours
- 📏 Threshold-based crowd density alerts
- 🧠 Simple, lightweight, and customizable
- 💻 Built using Python and OpenCV

---

## 🖥️ Demo Output

```
Crowd Detected: HIGH
Crowd Count: 67 contours detected
```

> A window will display the live feed with detected contours, and alerts are printed in the terminal if crowd density is high.

---

## 📁 Project Structure

```
Crowd-Detection/
│
├── crowd.py                # Main script to detect crowd
├── video.mp4               # Sample video file (optional)
├── requirements.txt        # Required Python libraries
└── README.md               # Project documentation
```

---

## ⚙️ Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Gayatrii4506/Crowd-Detection.git
cd Crowd-Detection
```

### Step 2: Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not available, manually install:

```bash
pip install opencv-python numpy
```

---

## ▶️ Usage

### To run with **webcam** input:

```bash
python crowd.py
```

### To run with a **video file**:

```bash
python crowd.py video.mp4
```

---

## 🔍 How It Works

1. **Video Input**: Captures video using OpenCV.
2. **Preprocessing**: Converts frame to grayscale and applies Gaussian blur.
3. **Thresholding**: Uses background subtraction and thresholding to detect movement.
4. **Contour Detection**: Detects object boundaries.
5. **Crowd Estimation**: Counts large contours.
6. **Alert**: Triggers a warning if contour count exceeds threshold.

---

## 🔧 Customization

- Modify `min_contour_area` to change what is considered a person/object.
- Adjust `crowd_threshold` for sensitivity of alerts.
- Add sound or email alert features as needed.

---

## 💡 Use Cases

- Public event monitoring
- Railway station surveillance
- Emergency crowd control
- Smart city infrastructure
- Religious gathering monitoring

---

## 👩‍💻 Author

**Gayatri Duse**  
GitHub: [@Gayatrii4506](https://github.com/Gayatrii4506)

---

## 📄 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute it.

---

## 🌟 Show Some Love

If you found this project useful, leave a ⭐ on the repo!
