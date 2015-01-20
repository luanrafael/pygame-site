angular.module("app").directive('pagination', function($rootScope,  posts_rest_api){
	return{
		templateUrl: '/static/js/src/directives/pagination/pagination_directive.html',
		restrict: "E",
		replace: "true",
		scope:{
			options: "="
		},
		link: function(scope, elm, atrrs){
			scope.getMorePosts = function(index){
				scope.options.getPosts(index);

			}
		}
	};
});
