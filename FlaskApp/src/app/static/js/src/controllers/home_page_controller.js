app.controller('homePageCtrl', function($scope, $rootScope, $window, PostsModel, posts_rest_api){
		"use strict";

		var model;
		$scope.model = model = PostsModel;
		$scope.pagination_options = {};

		$scope.getPosts = function(multiplier){
			var multiplier =  multiplier || 1;

			//TODO: essa lógica deveria
			//estar em outro lugar
			model.end = model.end * multiplier;

			if (multiplier !== 1){
				model.begin = model.begin + 5;
			}
			console.log(model.begin + " " + model.end);
			posts_rest_api.get(model.begin, model.end).success(function(result){
				$scope.isLoading = false;
				model.posts = result.data.reverse();
				$scope.pagination_options.pages = range(model.posts.length / 5);
				_transform_to_date(model.posts);
			}).error(function(err){
				console.log(err);
			});
		};

		$scope.pagination_options.getPosts = $scope.getPosts;

		$window.onload = function(){
			$scope.isLoading = true;
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
