# coding: utf-8

import json
from flask import Blueprint, jsonify, request, make_response
import usecase

posts_api = Blueprint("posts_api", __name__, url_prefix="/api/posts")


@posts_api.route("/add", methods=["POST"])
def add():
    data = json.loads(request.data)
    usecase.add_post(**data)

    return jsonify({})


@posts_api.route("/get", methods=["GET"])
def get():
    quantity = int(request.query_string.split("=")[1])
    posts = usecase.get_posts(quantity)

    data = [post.to_dict() for post in posts]
    return jsonify(data=data)


@posts_api.route("/delete", methods=["POST"])
def delete():
    _id = json.loads(request.data)["id"]

    usecase.delete_post(_id)
    return jsonify({})


@posts_api.route("/edit", methods=["POST"])
def edit():
    data = json.loads(request.data)
    id = data.pop("id")
    edited_post = usecase.edit_post(id, **data)

    if edited_post is None:
        response = make_response("post object does not exists")
        response.status_code = 500
        return response
    return jsonify(data=edited_post.to_dict())
