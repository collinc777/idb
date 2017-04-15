var updateGridAndPagination = null;
var updateSearchAndPagination = null;

var ajaxModel = {
    dataURL: null,
    modelURL: null,
    updateGridDataCallback: null,
    updatePaginationCallback: null,
    updateResultsDataCallback: null,
    onSearchPage: false,
    currentSearchQuery: null,
    currentPage: 1,
    currentSortParam: "name",
    currentSortAscending: 1,
    currentFilterText: null,
    getJSON: function(url, successCallback){
        console.log("Calling getWithJSON on URL: " + url);
        var settings = {
            url: url,
            success: successCallback,
            dataType: "json"
        };
        $.get(settings);
    },
    applyPageSortFilter: function(){
        if(this.dataURL === null){
            window.alert("DataURL is undefined, cannot filter");
        }else{
            console.log("Page: " + this.currentPage + ", sort: " + this.currentSortParam);
            console.log("Filter: " + this.currentFilterText);

            var url = this.dataURL;
            url += "?page=" + this.currentPage;
            if(this.currentFilterText !== null){
                url += "&filterText=" + this.currentFilterText;
            }
            if(this.currentSortParam !== null){
                url += "&sortParam=" + this.currentSortParam;
                url += "&sortAscending=" + this.currentSortAscending;
            }
            this.getJSON(url, updateGridAndPagination);
        }
    },
    applySearchPage: function(){
        if(this.dataURL === null){
            window.alert("DataURL is undefined, cannot filter");
        }else{
            console.log("Page: " + this.currentPage);

            var url = this.dataURL;
            url += "?query=" + this.currentSearchQuery;
            url += "&page=" + this.currentPage;
            
            this.getJSON(url, updateSearchAndPagination);
        }
    },
    sortData: function(field, ascending){
        this.currentSortParam = field;
        this.currentSortAscending = ascending;
        this.currentPage = 1;
        
        this.applyPageSortFilter();
    },
    filterData: function(filterText){
        this.currentFilterText = filterText;
        this.currentPage = 1;

        this.applyPageSortFilter();
    },
    setCurrentPage: function(page){
        this.currentPage = page;

        if(this.onSearchPage){
            this.applySearchPage();
        }else{
            this.applyPageSortFilter();
        }
    },
    highlightPropertyMatches: function(){
        console.log("Highlighting matches");
        var resultPropertyMatchValues = $(".resultPropertyMatchValue");
        var lowercaseQuery = this.currentSearchQuery.toLowerCase();

        resultPropertyMatchValues.each(function(){
            var originalElement = $(this);
            var originalText = originalElement.text();

            var newHTML = "";
            var words = originalText.split(/[ .,();]/);
            for(var i = 0; i < words.length; i++){
                var lowercaseWord = words[i].toLowerCase();

                if(lowercaseWord === (lowercaseQuery)){
                    var linkToProperty = originalElement.closest(".resultPropertyMatchRow").data("url");
                    newHTML += '<a href="' + linkToProperty + '" class="searchResultHighlight">' + words[i] + '</a>';
                }else{
                    newHTML += words[i];
                }
                newHTML += " ";
            }
            originalElement.html(newHTML);
        });
    }
};

// Define this down here because it needs to reference ajaxModel
updateGridAndPagination = function(dataOrError){
    console.log("Got data back: ");
    console.log(dataOrError);
    if(dataOrError["error"] !== undefined){
        window.alert("API request malformed: " + dataOrError["error"]);
    }else{
        console.log("Data successful, updating grid and pages");
        ajaxModel.updateGridDataCallback(dataOrError["modelData"]);
        ajaxModel.updatePaginationCallback(dataOrError["pageData"]);
    }
};

updateSearchAndPagination = function(dataOrError){
    console.log("Got data back: ");
    console.log(dataOrError);
    if(dataOrError["error"] !== undefined){
        window.alert("API request malformed: " + dataOrError["error"]);
    }else{
        console.log("Data successful, updating grid and pages");
        ajaxModel.updateResultsDataCallback(dataOrError["resultsData"]);
        ajaxModel.updatePaginationCallback(dataOrError["pageData"]);
    }
};

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
