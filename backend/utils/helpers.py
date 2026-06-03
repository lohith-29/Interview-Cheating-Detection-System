from datetime import datetime


def current_time():

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def response_message(
    success,
    message
):

    return {
        "success": success,
        "message": message
    }


def convert_object_id(data):

    if "_id" in data:
        data["_id"] = str(data["_id"])

    return data