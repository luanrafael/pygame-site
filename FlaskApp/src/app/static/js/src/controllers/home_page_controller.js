app.controller('homePageCtrl', function($scope, $rootScope, $window, PostsModel, posts_rest_api){
		"use strict";

		var model;
		$scope.model = model = PostsModel;
		$scope.pagination_options = {};

		$scope.getPosts = function(index){
			var begin = 5 * (index -1);

			posts_rest_api.get(begin).success(function(result){
				$scope.isLoading = false;
				model.posts = result.data.reverse();
				_transform_to_date(model.posts);
			}).error(function(err){
				console.log(err);
			});
		};

		$scope.pagination_options.getPosts = $scope.getPosts;

		$window.onload = function(){
			$scope.isLoading = true;
			posts_rest_api.count().success(function(result){
				model.quantity = result.data.quantity;
				$scope.pagination_options.pages = range(model.quantity / 5);
			});

			$scope.getPosts(1);
		};

		$window.onscroll = function(){
			if ($window.pageYOffset > 165){} // TODO: terminar de implementar
		};

		var range = function(number){
			// TODO: transformar em filtro
			var list = [1];
			for(var i = 1;  i <= number; i++){
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
);
