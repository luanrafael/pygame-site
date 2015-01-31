angular.module("app").service("PostsModel", function(){
	"use strict";

	var posts_model = {
		posts: [],
		quantity: 0
	}

	return posts_model;
});
