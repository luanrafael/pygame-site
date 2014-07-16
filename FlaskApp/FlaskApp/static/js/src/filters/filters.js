app.filter('sliceContent', function(){

	return function(input){
		return input.slice(0, 400);
	};
});