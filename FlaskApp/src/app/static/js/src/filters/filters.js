app.filter('sliceContent', function(){

	var html = '<a class="link" ng-click="showEntirePost()">Leia Mais</a>';

	return function(input){
		return input.slice(0, 400) + '...' + html;
	};
});