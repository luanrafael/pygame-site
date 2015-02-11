# coding: utf-8

import json
from flask import Blueprint, jsonify, request, make_response
import usecase
import utils

posts_api = Blueprint("posts_api", __name__, url_prefix="/api/posts")


@posts_api.route("/add", methods=["POST"])
def add():
    data = json.loads(request.data)
    usecase.add_post(**data)

    return jsonify({})


@posts_api.route("/get", methods=["GET"])
def get():
	request_dict = utils.parse_from_query_string(request.query_string)

	begin = int(request_dict["begin"])

	posts = usecase.get_posts(begin)

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

@posts_api.route("/count", methods=["GET"])
def count():
	quantity = usecase.count_posts()
	return jsonify(data={"quantity": quantity})
