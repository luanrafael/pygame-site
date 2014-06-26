app.controller('adminCtrl', ['$scope', 'posts_rest_api', function($scope, posts_rest_api){

	$scope.show_success_post_message = false;
	$scope.show_error_post_message = false;
	
	$scope.addPost = function(){
		var data = {
			author: "author",
			content: $scope.content,
			title: $scope.title
		};
		posts_rest_api.add_post(data).success(function(){
			$scope.show_success_post_message = true;
		}).error(function(){
			$scope.show_error_post_message = true;
		});
	};

}]);