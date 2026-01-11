def detect_text_emotion(text):
    text = text.lower()

    if any(word in text for word in ["sad", "tired", "angry", "stress"]):
        return "sad"
    elif any(word in text for word in ["happy", "good", "excited"]):
        return "happy"
    else:
        return "neutral"
