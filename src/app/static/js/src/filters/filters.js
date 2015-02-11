angular.module("app").filter('sliceContent', function($compile){
    'use strict';

	return function(input){
        if (input.length >= 1000) {
            return input.slice(0, 1000) + ' ...';
        }else{
            return input;
        }
	};
});
