from flask import request


def detect_tab_switch():

    data = request.json

    status = data.get(
        "tab_switched",
        False
    )

    return status