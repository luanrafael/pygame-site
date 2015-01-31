angular.module("app").directive("loader", function(){
    'use strict';
	return{
		restrict: "E",
		replace: true,
		templateUrl: '/static/js/src/directives/loaders/loader.html'
	};
});