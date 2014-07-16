app.directive("post", function(){

	return{
		restrict: "E",
		replace: "true",
		templateUrl: "/static/js/src/directives/post/post_directive.html",
		scope:{
			postOptions: "=",
			disableAllPosts: "&"
		},
		link: function  (scope, elm, attrs) {

			if (!scope.postOptions.imageUrl)
				scope.postOptions.imageUrl = "https://ssl.gstatic.com/android/market/org.renpy.pygame/hi-256-0-f5e1585ebee41805d202108d090517067fdccdfd";

			var showSinglePost = false;
			scope.commentsMessage = 'visualizar Comentários';

			scope.showSinglePost = function(){
				if (showSinglePost){
					scope.disableAllPosts(true, scope.postOptions);
					showSinglePost = false;
					scope.commentsMessage = 'visualizar Comentários';
				}else{
					scope.disableAllPosts(false, scope.postOptions);
					showSinglePost = true;
					scope.commentsMessage = 'esconder Comentários';
				}
			};
		}
	};
});