import json
from flask import Blueprint, jsonify, request
from FlaskApp.models.post import Post
from FlaskApp.models.db_init import init_db

__author__ = 'iury'

init_db()
posts_api = Blueprint("posts_api", __name__)

@posts_api.route("/posts/get_all_posts", methods=["GET"])
def get_all_posts():
    posts = Post.select()
    posts = [post.to_dict() for post in posts]
    return jsonify({'posts': posts})


@posts_api.route("/posts/add_post", methods=["POST"])
def add_post():
	print request.json
	author = request.json['author']
	content = request.json['content']
	title = request.json['title']

	Post.save_post(author, content, title)
	return jsonify(request.json)

