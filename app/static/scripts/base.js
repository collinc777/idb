var updateGridAndPagination = null;
var updateSearchAndPagination = null;

var ajaxModel = {
    dataURL: null,
    modelURL: null,
    modelLinks: window.allModelLinks,
    updateGridDataCallback: null,
    updatePaginationCallback0: null,
    updatePaginationCallback1: null,
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
    capitalizeWord: function(word){
        return word.charAt(0).toUpperCase() + word.slice(1);
    },
    highlightPropertyMatches: function(){
        var resultPropertyMatchValues = $(".resultPropertyMatchValue");
        var queryWords = this.currentSearchQuery.split(/[\s]/gi);

        resultPropertyMatchValues.each(function(){
            var originalElement = $(this);
            var originalText = originalElement.text();
            var linkToProperty = originalElement.closest(".resultPropertyMatchRow").data("url");
            var newHTML = "";

            var compoundHighlightRegexes = [];
            for(var i = 0; i < queryWords.length; i++){
                compoundHighlightRegexes.push('(\\b' + queryWords[i] + '\\b)');
            }
            compoundHighlightRegexes.push();

            compoundHighlightRegexes = compoundHighlightRegexes.join("|")
            console.log("compoundHighlightRegexes: ");
            console.log(compoundHighlightRegexes);

            var highlightRe = new RegExp(compoundHighlightRegexes, "gi");
            console.log(highlightRe.toString());
            var matches = originalText.match(highlightRe);
            console.log(matches);
            var replaceRe = '<a href="' + linkToProperty + '" class="searchResultHighlight">$&</a>';
            var newHTML = originalText.replace(highlightRe, replaceRe);            

            console.log(newHTML);

            // if(matches){
            //     console.log(matches);
            //     for(var i = 1; i < matches.length; i++){
                    
            //     }
            // }

            // window.alert("Hi");

            // // ? lookahead keeps the delimiters (punctuation) as part of the string
            // for(var i = 0; i < words.length; i++){
            //     var wordMatchesAnyQuery = false;
            //     for(var j = 0; j < lowercaseQueryWords.length; lowercaseQueryWords++){
            //         if(lowercaseWord === lowercaseQueryWords[j].trim()){
            //             wordMatchesAnyQuery = true;
            //             break;
            //         }
            //     }

            //     if(wordMatchesAnyQuery === true){
                    
            //         newHTML += ;
            //     }else{
            //         newHTML += words[i];
            //     }
            // }
            originalElement.html(newHTML);
        });
    },
    scrollToSelectedProperty: function(elementID){
        if(elementID !== undefined && elementID.length > 1){
            var selectedElement = $(elementID);

            if(selectedElement !== undefined && selectedElement !== null){
                var selectedPropertyOffset = selectedElement.offset()["top"];
                $("body").animate({scrollTop: selectedPropertyOffset - 50}, {complete: function(){
                    console.log("Finished scrolling: " + selectedPropertyOffset);
                }});
            }else{
                console.log(selectedElement);
            }
        }
    },
    callUpdatePaginationCallbacks: function(pageData){
        this.updatePaginationCallback0(pageData);
        if(this.updatePaginationCallback1 !== null){
            this.updatePaginationCallback1(pageData);
        }
    },
    getModelLink: function(modelLinkString, propertyKey){
        var modelLink = this.modelLinks[modelLinkString];
        console.log("Getting " + modelLinkString + "[" + propertyKey + "]");
        if(modelLink !== undefined && modelLink !== null && propertyKey in modelLink){
            return modelLink[propertyKey];
        }
        
    },
    getImageURL: function(modelURL, modelID){
        var convert = {
            characters: ["chars/", ".jpg"],
            houses: ["houses/", ".png"],
            books: ["books/", ".jpg"],
            alliances: ["alliances/", ".png"]
        };

        imgInfo = convert[modelURL.slice(1)];
        return "/static/img/" + imgInfo[0] + modelID + imgInfo[1];
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
        ajaxModel.callUpdatePaginationCallbacks(dataOrError["pageData"]);
        ajaxModel.updateGridDataCallback(dataOrError["modelData"]);
    }
};

updateSearchAndPagination = function(dataOrError){
    console.log("Got data back: ");
    console.log(dataOrError);
    if(dataOrError["error"] !== undefined){
        window.alert("API request malformed: " + dataOrError["error"]);
    }else{
        console.log("Data successful, updating grid and pages");
        ajaxModel.callUpdatePaginationCallbacks(dataOrError["pageData"]);
        ajaxModel.updateResultsDataCallback(dataOrError["resultsData"]);
    }
};

$(window).on("load", function(){
    $("#searchButton").on("click", function(event){
        event.preventDefault();
        var searchBarText = $("#searchBar").val();

        var redirectURL = "/search?query=" + searchBarText;
        window.location.replace(redirectURL);
    });
    $("#smallSearchButton").on("click", function(event){
        event.preventDefault();
        var searchBarText = $("#smallSearchBar").val();

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
