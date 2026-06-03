from flask import jsonify

from models.violation_model import violations


def dashboard():

    total = violations.count_documents({})

    return jsonify({
        "total_violations": total
    })