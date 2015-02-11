app.controller('adminCtrl', ['$scope', 'posts_rest_api', 'content_rest_api', function($scope, posts_rest_api, content_rest_api){

	$scope.show_success_post_message = false;
	$scope.show_error_post_message = false;
	$scope.actions = ['newPost', 'managePosts', 'manageDownloads'];
	$scope.posts = [];

    $scope.data = {};
    $scope.data.configEditor = {
    	height:'150'
    };

    $scope.data.selection = $scope.actions[0];
    $scope.data.categorie = 'pygame';
    $scope.data.isEditing = false;
    $scope.data.actual_id = null;
	$scope.$watch('data.selection', function(){
		if ($scope.data.selection === 'managePosts'){
			posts_rest_api.get(10).success(function(result){
				$scope.posts = result.posts.reverse();
				_transform_to_date($scope.posts);
			}).error(function(err){
				console.log(err);
			});
		}
	});

	$scope.changePostAction = function(action){
		$scope.data.selection = action;
	};

    $scope.editPost = function(post){
      $scope.data.selection = 'newPost';
      $scope.data.title = post.title;
      $scope.data.content = post.content;
      $scope.data.isEditing = true;
      $scope.data.actual_id = post.id;

    };

    $scope.addContent = function(content){
    	type = "download";
    	var data = {
    		content: content,
    		type: type
    	};
    	content_rest_api.add(data);
    };

    $scope.deletePost = function(id, index){
        $scope.posts.splice(index, 1);
        posts_rest_api.delete( {id:id} );
    };
	
	$scope.addPost = function(editing){
		var data = {
			author: g_user,
			content: $scope.data.content,
			title: $scope.data.title,
			categorie: $scope.data.categorie
		};

        if (editing){
            data.id = $scope.data.actual_id;
            $scope.data.isEditing = false;
            $scope.data.actual_id = null;
            posts_rest_api.edit(data).success(function(){
                $scope.show_success_edit_message = true;
            }).error(function(){
                $scope.show_error_post_message = true;
            });
        }else{
            posts_rest_api.add(data).success(function(){
			    $scope.show_success_post_message = true;
		    }).error(function(){
			    $scope.show_error_post_message = true;
		    });
        }
        _clear_fields('categorie', 'title', 'content');
	};

	var _transform_to_date = function(list){
		for (var item =  0; item < list.length; item++)
			list[item].date = new Date(Date.parse(list[item].date));
	};

	var _clear_fields = function(){
		for (arg in arguments){
			attr = arguments[arg];
			$scope.data[attr] = '';
		}
	};

}]);
