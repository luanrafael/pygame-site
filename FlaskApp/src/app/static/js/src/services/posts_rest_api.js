
app.factory("posts_rest_api", ['$http', function($http){
	'use strict';

    var endpoint = '/posts';
	var get_all_posts_url = endpoint + '/get_all_posts';
	var add_post_url = endpoint + '/add_post';
    var delete_post_url = endpoint + '/delete_post';
    var edit_post_url = endpoint + '/edit_post';

	var get_all_posts = function(){
		return $http.get(get_all_posts_url);
	};

	var add_post = function(data){
		return $http.post(add_post_url, data);
	};

    var delete_post = function(data){
      return $http.post(delete_post_url, data);
    };

    var edit_post  = function(data){
        return $http.post(edit_post_url, data);
    }

	return {
		get_all_posts: get_all_posts,
		add_post: add_post,
        delete_post: delete_post,
        edit_post: edit_post
	};

}]);