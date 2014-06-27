from flask import Blueprint, jsonify, request
from FlaskApp.models.post import Post
from FlaskApp.models.db_config import init_db

__author__ = 'iury'

init_db()
posts_api = Blueprint("posts_api", __name__)

@posts_api.route("/get_all_posts", methods=["GET"])
def get_all_posts():
    posts = Post.select()
    posts = [post.to_dict() for post in posts]
    return jsonify({'posts': posts})


@posts_api.route("/add_post", methods=["POST"])
def add_post():
    author = request.json['author']
    content = request.json['content']
    title = request.json['title']

    Post.save_post(author, content, title)
    return jsonify(request.json)


@posts_api.route("/delete_post", methods=["POST"])
def delete_post():
    id = request.json['id']
    Post.delete_post(id)
    return jsonify({})


@posts_api.route("/edit_post", methods=["POST"])
def edit_post():
    id = request.json.pop('id')
    Post.edit_post(id, request.json)
    return jsonify({})


