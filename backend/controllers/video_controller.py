from flask import request, jsonify

from services.face_detection import detect_face
from services.multiple_face_detection import detect_multiple_faces
from services.phone_detection import detect_phone


def analyze_frame():

    file = request.files["image"]

    image_bytes = file.read()

    face = detect_face(image_bytes)

    multiple = detect_multiple_faces(
        image_bytes
    )

    phone = detect_phone(
        image_bytes
    )

    return jsonify({
        "face": face,
        "multiple_faces": multiple,
        "phone": phone
    })