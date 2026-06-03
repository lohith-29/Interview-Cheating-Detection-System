from ultralytics import YOLO

model = YOLO(
    "ml_models/yolov8_phone_detection.pt"
)


def detect_phone(file):

    results = model.predict(
        source=file,
        verbose=False
    )

    for result in results:

        for box in result.boxes:

            cls = int(box.cls[0])

            if cls == 67:
                return True

    return False