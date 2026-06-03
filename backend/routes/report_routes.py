from flask import Blueprint

from controllers.report_controller import (
    get_reports
)

report_bp = Blueprint(
    "report",
    __name__
)

report_bp.route(
    "/reports",
    methods=["GET"]
)(get_reports)