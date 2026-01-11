stress_counter = {}

def emotion_based_action(emotion):
    if emotion in ["sad", "angry", "fear"]:
        return "Suggest break or easier task"
    elif emotion in ["happy", "neutral"]:
        return "Continue current task"
    elif emotion == "surprise":
        return "Check user focus"
    else:
        return "No action"

def check_stress(employee_id, emotion):
    if emotion in ["sad", "angry"]:
        stress_counter[employee_id] = stress_counter.get(employee_id, 0) + 1
    else:
        stress_counter[employee_id] = 0

    if stress_counter[employee_id] >= 3:
        return "⚠ Stress Alert: Notify Manager"
    return None
