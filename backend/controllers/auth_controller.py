from flask import request, jsonify

from models.user_model import users


def register():

    data = request.json

    users.insert_one({
        "name": data["name"],
        "email": data["email"],
        "password": data["password"]
    })

    return jsonify({
        "message": "User Registered"
    })


def login():

    data = request.json

    user = users.find_one({
        "email": data["email"],
        "password": data["password"]
    })

    if user:
        return jsonify({
            "message": "Login Success"
        })

    return jsonify({
        "message": "Invalid Credentials"
    }), 401