from flask import Blueprint, jsonify, request
from src.usecase import posts_usecase

__author__ = 'iury'

posts_api = Blueprint("posts_api", __name__)


@posts_api.route("/posts/get_all_posts", methods=["GET"])
def get_all_posts():
    posts = posts_usecase.get_all_posts()
    return jsonify({'posts': posts, 'quant': len(posts)})


@posts_api.route("/posts/add_post", methods=["POST"])
def add_post():
    author = request.json['author']
    content = request.json['content']
    title = request.json['title']
    categorie = request.json['categorie']

    posts_usecase.save_post(author, content, title, categorie)
    return jsonify({})


@posts_api.route("/posts/delete_post", methods=["POST"])
def delete_post():
    _id = request.json['id']
    has_success_on_delete = posts_usecase.delete_post(_id)
    return jsonify({'has_success_on_delete': has_success_on_delete})


@posts_api.route("/posts/edit_post", methods=["POST"])
def edit_post():
    _id = request.json.pop('id')
    print request.json
    posts_usecase.edit_post(_id, request.json)
    return jsonify({})
