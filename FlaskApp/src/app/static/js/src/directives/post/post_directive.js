app.directive("post", function(){

	return{
		restrict: "E",
		replace: "true",
		templateUrl: "/static/js/src/directives/post/post_directive.html",
		scope:{
			postOptions: "=",
			selectedPost: "=",
			disableAllPosts: "&"
		},
		link: function  (scope, elm, attrs) {

			// TODO: deixar como arquivo  estatico
			if (!scope.postOptions.imageUrl)
				scope.postOptions.imageUrl = "https://ssl.gstatic.com/android/market/org.renpy.pygame/hi-256-0-f5e1585ebee41805d202108d090517067fdccdfd";

			scope.entirePost = false;

			scope.showEntirePost = function(){
				scope.entirePost = true;
			};
		}
	};
});
