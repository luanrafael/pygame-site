angular.module("app").factory("posts_rest_api", function($http){
	'use strict';

    var endpoint = '/api/posts';
	var get_url = endpoint + '/get';
	var add_post_url = endpoint + '/add';
    var delete_post_url = endpoint + '/delete';
    var edit_post_url = endpoint + '/edit';
    var count_posts_url = endpoint + '/count';

	var _get = function(begin, end){
		return $http.get(get_url, {
			params: {
				begin: begin,
				end: end
			}
		});
	};

	var _add = function(data){
		return $http.post(add_post_url, data);
	};

    var _delete = function(data){
      return $http.post(delete_post_url, data);
    };

    var _edit  = function(data){
        return $http.post(edit_post_url, data);
    };

    var _count = function(){
    	return $http.get(count_posts_url);
    };

	return {
		get: _get,
		add: _add,
        delete: _delete,
        edit: _edit,
        count: _count
	};

});
