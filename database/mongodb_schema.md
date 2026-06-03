# MongoDB Database Schema

Database Name:
interview_proctoring

----------------------------------------

Collection: users

{
    "_id": ObjectId,
    "name": "Lohith",
    "email": "lohith@gmail.com",
    "password": "hashed_password",
    "role": "candidate",
    "created_at": "2026-06-01"
}

----------------------------------------

Collection: violations

{
    "_id": ObjectId,
    "candidate_id": "123",
    "violation_type": "PHONE_DETECTED",
    "timestamp": "2026-06-01 10:30:00",
    "confidence": 0.95
}

----------------------------------------

Collection: reports

{
    "_id": ObjectId,
    "candidate_id": "123",
    "phone_detected": 2,
    "multiple_faces": 1,
    "tab_switches": 3,
    "gaze_violations": 4,
    "head_pose_violations": 2,
    "risk_score": 78,
    "status": "SUSPICIOUS"
}