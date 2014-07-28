	

app.controller('homePageCtrl', ['$scope','$rootScope', '$window', 'posts_rest_api', function($scope, $rootScope, $window, posts_rest_api){

	$scope.posts = [];
	$scope.filterPage = "1";
	$scope.posts_per_categorie = {'pygame': 0, 'pysdl': 0, 'pyj2d': 0};
	$scope.data = {};
	$scope.data.post_pages = [];

	$window.onload = function(){
		$scope.isLoading = true;
		_get_posts();
	};

	$window.onscroll = function(){
		if ($window.pageYOffset > 165){} // TODO: terminar de implementar
	};

	$scope.setCategorie = function(categorie){
		$scope.categorie = categorie;
		var elements = document.getElementsByName('tag')
		for (var element in elements){
			if (elements[element].id === categorie)
				elements[element].style.color = '#18bc9c';
			else
				elements[element].style.color = 'white';
		}
		

	};

	var _get_posts = function(){
		posts_rest_api.get_all_posts().success(function(result){
			$scope.isLoading = false;
			$scope.posts = result.posts.reverse();
			_split_posts_pages(result.quant);
			_transform_to_date($scope.posts);
			_count_post_categories();
		}).error(function(err){
			console.log(err);
		});
	};

	var _transform_to_date = function(list){
		for (var item =  0; item < list.length; item++){
			list[item].date = new Date(Date.parse(list[item].date));
		}
	};
	var _count_post_categories = function(){
		for (var i in $scope.posts){
			attr = $scope.posts[i].categorie;
			if (attr)
				$scope.posts_per_categorie[attr.toLowerCase()] ++;
		}
	};
	var _split_posts_pages = function(quant){
		range = (quant / 10) + 1;
		for(var i = 0; i < range; i++){
			$scope.data.post_pages.push(i);
		}

		$rootScope.$broadcast("post_pages_event", $scope.data);
	}
}]);