angular.module("app")
    .controller('homePageCtrl', function($scope, $rootScope, $window, PostsModel, posts_rest_api){
		"use strict";

		var model;
		$scope.model = model = PostsModel;
		$scope.pagination_options = {};
        $scope.showPagination = false;
        $scope.post_found = true;
        
		$scope.compareTitle = function(input, expected){

			if (!expected)
				return true;

			if (input.search(expected) == -1){
				$scope.post_found = false;
			}else{
				$scope.post_found  = true;
			}
			return $scope.post_found;
		};


		$scope.getPosts = function(index){
			var begin = 5 * (index -1);

			posts_rest_api.get(begin).success(function(result){
				$scope.isLoading = false;
				model.posts = result.data.reverse();
                if (model.posts.length > 5){
                    $scope.showPagination = true;
                }
				_transform_to_date(model.posts);
			}).error(function(err){
                $scope.isLoading = false;
				console.log(err);
			});
		};

		$scope.hasPosts = function(){
			return model.posts.length > 0;
		};

		$scope.pagination_options.getPosts = $scope.getPosts;
        $scope.pagination_options.scrollTop =  function(){
            jQuery('html, body').animate({
                scrollTop: jQuery("#top").offset().top
            }, 500);
        };

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
