app.controller('signInUpCtrl', ['$scope', '$timeout', function($scope, $timeout){

    $scope.classSignIn = 'form-signIn' + ' fade-in';
    $scope.classSignUp = 'form-signup' + ' fade-out';



    $scope.showSignUpScreen = function(){
       $timeout(function(){
              $scope.classSignIn = 'form-signIn' + ' fade-out';
       }, 50);
       $timeout(function(){
           $scope.classSignUp = 'form-signup' + ' fade-in';
       }, 100);
    } ;
}]);

