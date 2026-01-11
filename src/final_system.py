import cv2
from deepface import DeepFace

from .task_engine import emotion_based_action, check_stress
from .logger import log_emotion
from .text_emotion import detect_text_emotion

EMPLOYEE_ID = "EMP001"  # anonymized employee id

print("=== Emotion-Aware Employee System Started ===")

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

        # Log emotion
        log_emotion(EMPLOYEE_ID, emotion, "camera", action)

        # Stress check
        alert = check_stress(EMPLOYEE_ID, emotion)
        if alert:
            print(alert)

        cv2.putText(frame, f"Emotion: {emotion}", (30, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.putText(frame, f"Action: {action}", (30, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

        if alert:
            cv2.putText(frame, alert, (30, 120),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    except Exception as e:
        print("Error:", e)

    cv2.imshow("Final Emotion System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
