	

app.controller('homePageCtrl', ['$scope','$rootScope', '$window', 'posts_rest_api', 
	function($scope, $rootScope, $window, posts_rest_api){

		$scope.posts = [];
		$scope.filterPage = "1";
		$scope.data = {};
		$scope.data.post_pages = [];
		$scope.hasPostOnPage = true;

		$window.onload = function(){
			$scope.isLoading = true;
			_get_posts();
		};

		$window.onscroll = function(){
			if ($window.pageYOffset > 165){} // TODO: terminar de implementar
		};


		var _get_posts = function(){
			posts_rest_api.get(10).success(function(result){
				$scope.isLoading = false;
				$scope.posts = result.data.reverse();
				_transform_to_date($scope.posts);
			}).error(function(err){
				console.log(err);
			});
		};

		var _transform_to_date = function(list){
			for (var item =  0; item < list.length; item++){
				list[item].date = new Date(Date.parse(list[item].date));
			}
		};

	}
]);
