	

app.controller('homePageCtrl', ['$scope', '$window', 'posts_rest_api', function($scope, $window, posts_rest_api){

	$scope.posts = [];
	$scope.posts_per_categorie = {'pygame': 0, 'pysdl': 0, 'pyj2d': 0};
	$scope.post_pages = [];

	$window.onload = function(){
		data = {
			'start': 0,
			'end': 10
		};
		posts_rest_api.get_all_posts(data).success(function(result){
			$scope.posts = result.posts.reverse();
			_split_posts_pages(result.quant);
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
	var _split_posts_pages = function(quant){
		range = (quant / 10) + 1;
		for(var i = 0; i < range; i++)
			$scope.post_pages.push(i);
	}
}]);