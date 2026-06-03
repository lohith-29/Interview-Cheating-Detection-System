import cv2
import numpy as np


def read_frame(file):

    frame = cv2.imdecode(
        np.frombuffer(
            file.read(),
            np.uint8
        ),
        cv2.IMREAD_COLOR
    )

    return frame


def resize_frame(
    frame,
    width=640,
    height=480
):

    return cv2.resize(
        frame,
        (width, height)
    )


def convert_gray(frame):

    return cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )