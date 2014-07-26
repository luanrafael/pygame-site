app.directive("loader", function(){
	return{
		restrict: "E",
		replace: true,
		templateUrl: '/static/js/src/directives/loaders/loader.html'
	};
});