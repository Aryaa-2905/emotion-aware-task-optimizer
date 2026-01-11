# Emotion-Aware Task Optimizer 🧠📊

A real-time emotion-aware system that detects employee emotions using camera, text, and audio inputs, and intelligently recommends tasks while monitoring stress levels and team mood.


## 🚀 Features

- 🎥 Real-time facial emotion detection using **DeepFace + OpenCV**
- 💬 Text-based emotion analysis
- 🎧 Audio emotion processing (live module support)
- 🧠 Emotion-based task recommendations
- 📈 Emotion logging and stress monitoring
- 🚨 Automatic stress alerts for prolonged negative emotions
- 👥 Team-level mood analytics
- 🔒 Privacy-first approach with anonymized employee IDs


🏗️ Project Structure
emotion-aware-task-optimizer/
│
├── src/
│   ├── __init__.py
│   ├── final_system.py
│   ├── logger.py
│   ├── task_engine.py
│   ├── text_emotion.py
│
├── audio_emotion_live.py
├── camera_emotion.py
├── emotion_task_loop.py
├── team_mood_analytics.py
├── utils.py
│
├── requirements.txt
├── README.md
├── .gitignore


⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/Aryaa-2905/emotion-aware-task-optimizer.git
cd emotion-aware-task-optimizer

2️⃣ Create and activate virtual environment
python -m venv venv


Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ How to Run

Make sure your camera is connected.

python -m src.final_system


📸 A webcam window will open and display detected emotions in real time.

🧪 Example Output

Emotion detected: Happy / Neutral / Sad / Angry

Suggested action printed in terminal

Stress alerts triggered after repeated negative emotions

Logs stored for analytics

🛠️ Tech Stack

Python

OpenCV

DeepFace

TensorFlow / Keras

NumPy

Pandas

🔐 Data Privacy

Employee identity is anonymized

No facial images are stored

Only emotion labels and timestamps are logged

🚀 Future Enhancements

Web dashboard for HR

Email / Slack alerts

Speech emotion integration

Cloud deployment (FastAPI / Docker)

👩‍💻 Author

Arya Gahine
B.Tech ENTC | Data Science & AI
GitHub: https://github.com/Aryaa-2905

⭐ Acknowledgements

DeepFace library

OpenCV community

TensorFlow team