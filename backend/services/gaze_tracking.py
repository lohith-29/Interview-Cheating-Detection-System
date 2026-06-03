import cv2
import numpy as np


def detect_gaze_direction(face_center_x, frame_width):

    center_region_left = frame_width * 0.4
    center_region_right = frame_width * 0.6

    if face_center_x < center_region_left:
        return "LEFT"

    elif face_center_x > center_region_right:
        return "RIGHT"

    return "CENTER"


def gaze_violation(face_center_x, frame_width):

    direction = detect_gaze_direction(
        face_center_x,
        frame_width
    )

    if direction != "CENTER":
        return True

    return False