# coding: utf-8

import json
from flask import Blueprint, jsonify, request
import usecase

users_api = Blueprint("users_api", __name__, url_prefix="/api/users")

@users_api.route("/add", methods=["POST"])
def add():
    data = json.loads(request.data)
    usecase.add_user(**data)

    return jsonify({})

@users_api.route("/get_all", methods=["GET"])
def get_all():
    users = usecase.get_users()

    return jsonify(data=[user.to_dict() for user in users])

@users_api.route("/get_by_login", methods=["POST"])
def get_by_login():
    data = json.loads(request.data)
    user = usecase.get_user_by_login(data["login"])

    return jsonify(user.to_dict())

@users_api.route("/delete", methods=["POST"])
def delete():
    data = json.loads(request.data)
    usecase.delete_user(data["login"])

    return jsonify(data={})