	

app.controller('homePageCtrl', ['$scope', '$window', 'posts_rest_api', function($scope, $window, posts_rest_api){

	$scope.posts = [];
	$scope.posts_per_categorie = {'pygame': 0, 'pysdl': 0, 'pyj2d': 0};

	$window.onload = function(){
		posts_rest_api.get_all_posts().success(function(result){
			$scope.posts = result.posts.reverse();
			_transform_to_date($scope.posts);
			_count_post_categories();
		}).error(function(err){
			console.log(err);
		});
	};

	$window.onscroll = function(){
		if ($window.pageYOffset > 165){}
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
}]);