app.directive("postComments", function(){

	return{
		restrict: "E",
		replace: "true",
		templateUrl: "/static/js/src/directives/post_comments/post_comments.html",
		link: function(){
    		var disqus_shortname = 'pygamebr'; // required: replace example with your forum shortname
		    (function() {
		        var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
		        dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
		        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
		    })();
		}
	};
});