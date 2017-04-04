var updateGridData = null;

var ajaxModel = {
    dataURL: null,
    updateGridDataCallback: null,
    getJSON: function(url, successCallback){
        console.log("Calling getWithJSON on URL: " + url);
        var settings = {
            url: url,
            success: successCallback,
            dataType: "json"
        };
        $.get(settings);
    },
    sortData: function(field, ascending){
        if(this.dataURL === null){
            window.alert("DataURL is undefined, cannot sort");
        }else{
            var url = this.dataURL;
            url += "?page=10&offset=0";
            url += "&sortParam=" + field;
            url += "&sortAscending=" + ascending;
            this.getJSON(url, updateGridData);
        }
    },
    filterData: function(filterText){
        if(this.dataURL === null){
            window.alert("DataURL is undefined, cannot filter");
        }else{
            var url = this.dataURL;
            url += "?page=0&offset=0";
            url += "&filterText=" + filterText;
            this.getJSON(url, this.updateGridData);
        }
    }
};

// Define this down here because it needs to reference ajaxModel

updateGridData = function(dataOrError){
    console.log("Got data back: ");
    console.log(dataOrError);
    if(dataOrError["error"] !== undefined){
        window.alert("API request malformed: " + dataOrError["error"]);
    }else{
        console.log("Data successful, sending to updateGridDataCallback");
        ajaxModel.updateGridDataCallback(dataOrError);
    }
};