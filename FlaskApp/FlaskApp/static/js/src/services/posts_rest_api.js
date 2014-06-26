
app.factory("posts_rest_api", ['$http', function($http){
	'use strict';

	var get_all_posts_url = '/posts/get_all_posts';
	var add_post_url = '/posts/add_post';

	var get_all_posts = function(){
		return $http.get(get_all_posts_url);
	};

	var add_post = function(data){
		return $http.post(add_post_url, data);
	};

	return {
		get_all_posts: get_all_posts,
		add_post: add_post
	};

}]);