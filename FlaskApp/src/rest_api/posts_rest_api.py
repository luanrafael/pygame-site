from flask import Blueprint, jsonify, request
from FlaskApp.models.post import Post

__author__ = 'iury'

posts_api = Blueprint("posts_api", __name__)


@posts_api.route("/posts/get_all_posts", methods=["GET"])
def get_all_posts():
    posts = []
    ind = 1
    for post in Post.select().orderBy('date'):
        post_dict = post.to_dict()
        post_dict['ind'] = ind
        ind += 1

        posts.append(post_dict)
        if ind == 5:
            ind = 1

    return jsonify({'posts': posts, 'quant': len(posts)})


@posts_api.route("/posts/add_post", methods=["POST"])
def add_post():
    author = request.json['author']
    content = request.json['content']
    title = request.json['title']
    categorie = request.json['categorie']

    Post.save_post(author, content, title, categorie)
    return jsonify(request.json)


@posts_api.route("/posts/delete_post", methods=["POST"])
def delete_post():
    id = request.json['id']
    Post.delete_post(id)
    return jsonify({})


@posts_api.route("/posts/edit_post", methods=["POST"])
def edit_post():
    id = request.json.pop('id')
    Post.edit_post(id, request.json)
    return jsonify({})
