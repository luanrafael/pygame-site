

app.controller('homePageCtrl', ['$scope', '$window', 'posts_rest_api', function($scope, $window, posts_rest_api){

	$scope.posts = [];

	$window.onload = function(){
		posts_rest_api.get_all_posts().success(function(result){
			$scope.posts = result.posts.reverse();
			_transform_to_date($scope.posts);
		}).error(function(err){
			console.log(err);
		});
	};

	$window.onscroll = function(){
		if ($window.pageYOffset > 165)
			console.log($window.pageYOffset);
	};

	$scope.disableAllPosts = function(disable, post){
		if (disable){
			$scope.selectedPost = post.title;
			$scope.showComments = true;
		}else{
			$scope.selectedPost = '';
			$scope.showComments = false;
		}
	};

	var _transform_to_date = function(list){
		for (var item =  0; item < list.length; item++){
			list[item].date = new Date(Date.parse(list[item].date));
		}
	};
}]);