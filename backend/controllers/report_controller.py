from flask import jsonify

from models.report_model import reports


def get_reports():

    data = []

    for report in reports.find():

        report["_id"] = str(
            report["_id"]
        )

        data.append(report)

    return jsonify(data)