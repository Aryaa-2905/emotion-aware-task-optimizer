import streamlit as st
import cv2
from deepface import DeepFace

# ---------------- SESSION STATE ----------------
if "last_emotion" not in st.session_state:
    st.session_state.last_emotion = None

# ---------------- TASK RECOMMENDATION ----------------
def recommend_task(emotion):
    task_map = {
        "happy": "Creative brainstorming or collaborative tasks",
        "neutral": "Routine analytical or documentation work",
        "sad": "Light tasks, review work, or short breaks",
        "angry": "Avoid critical decisions, take a short pause",
        "fear": "Supportive tasks or one-on-one discussions",
        "surprise": "Exploratory or learning-oriented tasks",
        "disgust": "Non-interactive or independent tasks"
    }
    return task_map.get(emotion, "General productive work")

# ---------------- STREAMLIT UI ----------------
st.set_page_config(page_title="Emotion-Aware Task Optimizer")
st.title("🧠 Emotion-Aware Task Optimizer")
st.write("Real-time emotion detection using webcam")

run = st.checkbox("Start Camera")

frame_window = st.image([])
emotion_placeholder = st.empty()
task_placeholder = st.empty()

# ---------------- CAMERA LOGIC ----------------
if run:
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            st.warning("Camera not accessible")
            break

        try:
            result = DeepFace.analyze(
                frame,
                actions=["emotion"],
                enforce_detection=False
            )

            emotion = result[0]["dominant_emotion"]

            # Show only if emotion changes
            if emotion != st.session_state.last_emotion:
                st.session_state.last_emotion = emotion

                emotion_placeholder.success(f"Detected Emotion: {emotion}")
                task = recommend_task(emotion)
                task_placeholder.info(f"Recommended Task: {task}")

        except Exception:
            emotion_placeholder.warning("Detecting emotion...")

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_window.image(frame)

else:
    st.write("Camera stopped")
