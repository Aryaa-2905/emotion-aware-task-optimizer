import cv2
from deepface import DeepFace
from src.task_engine import emotion_based_action

print("Starting Emotion-Aware Task Optimizer...")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not accessible")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        result = DeepFace.analyze(
            frame,
            actions=["emotion"],
            enforce_detection=False
        )

        emotion = result[0]["dominant_emotion"]
        action = emotion_based_action(emotion)

        cv2.putText(frame, f"Emotion: {emotion}", (30, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.putText(frame, f"Action: {action}", (30, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    except Exception as e:
        print("Error:", e)

    cv2.imshow("Emotion-Aware Task Optimizer", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

