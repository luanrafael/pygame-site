app.filter('sliceContent', function($compile){

	return function(input){
		return input.slice(0, 1000) + '...';
	};
});
