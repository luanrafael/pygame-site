
app.factory("content_rest_api", ['$http', function($http){
	'use strict';

    var endpoint = '/content';
	var add_content_url = endpoint + '/add_content';

	var add_content = function(data){
		console.log(data);
		return $http.post(add_content_url, data);
	};

	return {
		add_content: add_content,
	};
}]);