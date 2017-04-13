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
    currentSortParam: "Name",
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
