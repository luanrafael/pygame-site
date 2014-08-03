# coding: utf-8

from flask import Blueprint, jsonify, request
from src.usecase import content_usecase

__author__ = 'iury'

contents_api = Blueprint("contents_api", __name__)

@contents_api.route("/content/add_content", methods=["POST"])
def add_content():
	content = request.json["content"]
	_type = request.json["type"]
	content_usecase.add_content(content, _type)
	return jsonify({})

@contents_api.route("/content/get_content", methods=["GET"])
def get_content():
	content = request.json["type"]
	content_usecase.add_content(content, _type)
	return jsonify({})

