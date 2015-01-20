var app = angular.module("app", ["ngCkeditor"]);

app.config(function($interpolateProvider){
	$interpolateProvider.startSymbol('{');
	$interpolateProvider.endSymbol('}');
});
