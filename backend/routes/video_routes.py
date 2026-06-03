from flask import Blueprint

from controllers.video_controller import (
    analyze_frame
)

video_bp = Blueprint(
    "video",
    __name__
)

video_bp.route(
    "/analyze",
    methods=["POST"]
)(analyze_frame)