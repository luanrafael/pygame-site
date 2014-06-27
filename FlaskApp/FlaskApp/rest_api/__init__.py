'''
Module containing all rest apis
Each rest api must be register in the __main__ file with the method register_blueprint
the rest api must follow this base structure

    from flask import Blueprint, jsonify

    api_name = Blueprint("api_name", __name__)

    @api_name.route("/url_prefix/endpoint", methods=["GET"])
    def function():
        return jsonify({"hello": "world"})


The method route receive two params:
    -> a string which is the url to map
    -> a list of allowed methods for the request, commonly used are 'POST', 'GET', 'PUT', 'DELETE'

url_prefix is the common url for all routes in the file
endpoint is a suggestive for the operation that the function does

each function must have a suggestive name and  must return a json, using the function jsonify
'''

__author__ = 'iury'


