def calculate_risk_score(
    phone_detected,
    multiple_faces,
    gaze_violations,
    tab_switches,
    head_pose_violations
):

    score = 0

    if phone_detected:
        score += 40

    if multiple_faces:
        score += 30

    score += gaze_violations * 5

    score += tab_switches * 10

    score += head_pose_violations * 5

    if score > 100:
        score = 100

    return score


def classify_candidate(score):

    if score < 30:
        return "SAFE"

    elif score < 70:
        return "WARNING"

    return "SUSPICIOUS"