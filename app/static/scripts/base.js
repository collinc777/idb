$(document).ready(function(){
	$("#searchButton").on("click", function(event){
		event.preventDefault();
		var searchBarText = $("#searchBar").val();

		var redirectURL = "/search?query=" + searchBarText;
		window.location.replace(redirectURL);
	});
	$("#frontSearchButton").on("click", function(event){
		event.preventDefault();
		var searchBarText = $("#frontSearchBar").val();

		var redirectURL = "/search?query=" + searchBarText;
		window.location.replace(redirectURL);
	});
});