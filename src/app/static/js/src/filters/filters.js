app.filter('sliceContent', function($compile){

	var html = ""//'<a class="link" ng-click="showEntirePost()">Leia Mais</a>';
		
	return function(input){
		return input.slice(0, 1000) + '...' + html;
	};
});
