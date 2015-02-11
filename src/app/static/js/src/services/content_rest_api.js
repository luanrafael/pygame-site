angular.module("app").factory("content_rest_api", ['$http', function($http){
	'use strict';

    var endpoint = '/api/contents';
	var add_content_url = endpoint + '/add';
	var get_content_url = endpoint + '/get';

	var add_content = function(data){
		return $http.post(add_content_url, data);
	};

	var get_content = function(type){
		var data = {
			type: type
		};
		return $http.get(get_content_url, data);
	};

	return {
		add_content: add_content,
		get_content: get_content
	};
}]);