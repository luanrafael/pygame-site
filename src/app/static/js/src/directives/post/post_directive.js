angular.module("app").config(function($sceProvider){
	$sceProvider.enabled(false);
});
angular.module("app").directive("post", function($compile, $timeout){

	return{
        transclude: true,
		restrict: "E",
		templateUrl: "/static/js/src/directives/post/post_directive.html",
		scope:{
			postOptions: "=",
			selectedPost: "=",
			disableAllPosts: "&"
		},
		link: function  (scope, elm) {
            scope.entirePost = false;

            // TODO: deixar como arquivo  estatico
            if (!scope.postOptions.imageUrl) {
                scope.postOptions.imageUrl = "https://ssl.gstatic.com/android/market/org.renpy.pygame/hi-256-0-f5e1585ebee41805d202108d090517067fdccdfd";

            }
            var showMoreLink = '<a class="link" ng-click="showEntirePost()" ng-show="!entirePost">Leia Mais</a>';

            if (scope.postOptions.content.length >= 1000) {
                var el = $compile(showMoreLink)(scope);
                $timeout(function () {
                    elm[0].getElementsByTagName("p")[0].firstChild.appendChild(el[0]);
                }, 0);
            }
			scope.showEntirePost = function(){
				scope.entirePost = true;
      			
			};
		}
	};
});
