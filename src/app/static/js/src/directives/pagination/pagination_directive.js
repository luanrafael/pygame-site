angular.module("app").directive('pagination', function($timeout){
	return{
		templateUrl: '/static/js/src/directives/pagination/pagination_directive.html',
		restrict: "E",
		replace: "true",
		scope:{
			options: "="
		},
		link: function(scope){
			scope.getMorePosts = function(index){
                scope.options.scrollTop();
                $timeout(function(){
                    scope.options.getPosts(index + 1);
                }, 600);
			};
		}
	};
});
