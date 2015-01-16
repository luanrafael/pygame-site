app.directive('pagination', function($rootScope){
	return{
		templateUrl: '/static/js/src/directives/pagination/pagination_directive.html',
		restrict: "E",
		replace: "true",
		scope:{
			options: "=",
			show: "="
		},
		link: function(scope, element, attrs){
			scope.showPagination = false;
			scope.filterByPage = function(page){
				page = page + 1;
				scope.filterPage = page.toString();
			}
		}
	};
});
