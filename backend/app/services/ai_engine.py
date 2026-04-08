def ai_decision(data):
    score = 0

    score += (data["heart_rate"] - 60) / 60
    score += (data["gas"] - 100) / 400

    if data["motion"] != "Normal":
        score += 1

    if score > 0.8:
        return "Critical"
    elif score > 0.5:
        return "Warning"
    return "Safe"