import json
from flask import Blueprint, jsonify
from FlaskApp.models.post import Post


__author__ = 'iury'


posts_api = Blueprint("posts_api", __name__)

@posts_api.route("/posts/get_all_posts")
def get_all_posts():
    posts = Post.select()
    posts = [post.to_dict() for post in posts]
    return jsonify({'posts':posts})




