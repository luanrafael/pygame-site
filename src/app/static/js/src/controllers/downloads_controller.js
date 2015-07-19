angular.module("app").controller('downloadsCtrl', ['$scope', '$window', 'content_rest_api',
    function($scope, $window, content_rest_api){
        'use strict';

        $window.onload = function(){
            content_rest_api.get_content("download").success(function(result){
                $scope.content = result.data;
            });
        };
}]);