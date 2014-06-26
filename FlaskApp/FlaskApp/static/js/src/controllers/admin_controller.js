app.controller('adminCtrl', ['$scope', 'posts_rest_api', function($scope, posts_rest_api){

	$scope.show_success_post_message = false;
	$scope.show_error_post_message = false;
	$scope.post_actions = ['newPost', 'managePosts'];
	$scope.posts = [];
	$scope.selection = $scope.post_actions[0];

	$scope.$watch('selection', function(){
		if ($scope.selection === 'managePosts'){
			posts_rest_api.get_all_posts().success(function(result){
				$scope.posts = result.posts.reverse();
				_transform_to_date($scope.posts);
			}).error(function(err){
				console.log(err);
			});
		}
	});

	$scope.changePostAction = function(action){
		$scope.selection = action;
	};
	
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

	var _transform_to_date = function(list){
		for (var item =  0; item < list.length; item++)
			list[item].date = new Date(Date.parse(list[item].date));
	};

}]);