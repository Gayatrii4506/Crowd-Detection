import cv2
from tkinter import *
from PIL import Image, ImageTk
from ultralytics import YOLO
from playsound import playsound
import threading

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Setup GUI window
window = Tk()
window.title("AI Crowd Monitoring System")
window.geometry("900x700")
window.configure(bg="white")

# Global variables
alert_played = False
cap = cv2.VideoCapture("http://192.0.0.4:8080/video")  # Use 0 for webcam or "crowd_video.mp4"

# GUI elements
video_label = Label(window)
video_label.pack()

count_label = Label(window, text="People Count: 0", font=("Arial", 16), bg="white")
count_label.pack(pady=10)

status_label = Label(window, text="Crowd Status: Low", font=("Arial", 16), bg="white")
status_label.pack(pady=10)

def monitor_video():
    global alert_played

    ret, frame = cap.read()
    if not ret:
        return

    # Predict
    results = model(frame)
    person_count = 0

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            if model.names[cls] == "person":
                person_count += 1
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Determine status
    if person_count < 5:
        status = "Low"
        color = "green"
        alert_played = False
    elif person_count < 10:
        status = "Medium"
        color = "orange"
        alert_played = False
    else:
        status = "High - ALERT!"
        color = "red"
        if not alert_played:
            threading.Thread(target=playsound, args=('alert.mp3',), daemon=True).start()
            alert_played = True

    # Update labels
    count_label.config(text=f"People Count: {person_count}")
    status_label.config(text=f"Crowd Status: {status}", fg=color)

    # Convert frame to ImageTk
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame_rgb)
    imgtk = ImageTk.PhotoImage(image=img)

    video_label.imgtk = imgtk
    video_label.configure(image=imgtk)
    video_label.after(10, monitor_video)

# Start the monitoring loop
monitor_video()

# Run the GUI loop
window.mainloop()

# Release video on exit
cap.release()
cv2.destroyAllWindows()
