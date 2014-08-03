app.controller('adminCtrl', ['$scope', '$window', 'content_rest_api', function($scope, $window, content_rest_api){

	$window.onload = function(){
		content_rest_api.get_content("download").success(function(result){
			$scope.content = result;
		});
	};

}]);