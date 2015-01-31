angular.module("app").filter('sliceContent', function($compile){
    'use strict';

	return function(input){
		return input.slice(0, 1000) + '...';
	};
});
