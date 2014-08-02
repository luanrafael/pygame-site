	

app.controller('homePageCtrl', ['$scope','$rootScope', '$window', 'posts_rest_api', function($scope, $rootScope, $window, posts_rest_api){

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

	$scope.$watch("search", function(){
		if ($scope.search.length > 0)
			$scope.hasPostOnPage = true;
	});

	var _get_posts = function(){
		posts_rest_api.get_all_posts().success(function(result){
			$scope.isLoading = false;
			$scope.posts = result.posts.reverse();
			_split_posts_pages(result.quant);
			_transform_to_date($scope.posts);
			_count_post_categories();
		}).error(function(err){
			console.log(err);
		});
	};

	var _transform_to_date = function(list){
		for (var item =  0; item < list.length; item++){
			list[item].date = new Date(Date.parse(list[item].date));
		}
	};

	var _split_posts_pages = function(quant){
		range = (quant / 10) + 1;
		for(var i = 0; i < range; i++){
			$scope.data.post_pages.push(i);
		}

		$rootScope.$broadcast("post_pages_event", $scope.data);
	}
}]);