angular.module("app").service("PostsModel", function(){
	"use strict";

	var posts_model = {
		posts: [],
		begin: 0,
		end: 5,
	}

	return posts_model;
});
