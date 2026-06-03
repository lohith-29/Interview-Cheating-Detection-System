import cv2
import numpy as np


def estimate_head_pose(face_x, frame_width):

    left_limit = frame_width * 0.35
    right_limit = frame_width * 0.65

    if face_x < left_limit:
        return "LOOKING_LEFT"

    elif face_x > right_limit:
        return "LOOKING_RIGHT"

    return "LOOKING_FORWARD"


def head_pose_violation(face_x, frame_width):

    pose = estimate_head_pose(
        face_x,
        frame_width
    )

    return pose != "LOOKING_FORWARD"