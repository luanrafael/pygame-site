app.controller('homePageCtrl', ['$scope','$rootScope', '$window', 'posts_rest_api', 
	function($scope, $rootScope, $window, posts_rest_api){
		"use strict";

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
				$scope.data.pages = range($scope.posts.length / 5);
				_transform_to_date($scope.posts);
			}).error(function(err){
				console.log(err);
			});
		};

		$scope.hasPagination = function(){
			return $scope.posts.length >= 5;
		};

		var range = function(number){
			// transformar em diretiva
			var list = [];
			for(var i = 0;  i < number; i++){
				list.push(number);
			}
			return list;
		};

		var _transform_to_date = function(list){
			for (var item =  0; item < list.length; item++){
				list[item].date = new Date(Date.parse(list[item].date));
			}
		};
	}
]);
