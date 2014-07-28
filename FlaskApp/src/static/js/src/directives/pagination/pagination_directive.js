app.directive('pagination', function($rootScope){
	return{
		templateUrl: '/static/js/src/directives/pagination/pagination_directive.html',
		restrict: "E",
		replace: "true",
		scope:{
			morePosts: "&",
			filterPage: "="
		},
		link: function(scope, element, attrs){
			scope.showPagination = false;

			$rootScope.$on("post_pages_event", function(ngEvent, data){
				scope.postPages = data.post_pages;

				if (scope.postPages.length >= 2){
					scope.showPagination = true;
				}
			});

			scope.filterByPage = function(page){
				page = page + 1;
				scope.filterPage = page.toString();
			}
		}
	};
});