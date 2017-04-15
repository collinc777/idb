class SearchQueryLayout extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            query: props.query
        }
    }

    render() {
        return (<div className="text-center">
            <h1 className="cursive listingTitle">"{this.state.query}"</h1>
            <br/>
        </div>);
    }
}

class SearchContainer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            query: props.query,
            numberOfResults: props.numberOfResults,
            pageData: props.pageData,
            searchResultsData: props.searchResultsData
        }
    }

    render() {
        return (
                <div>
                    <SearchQueryLayout query={this.state.query} numberOfResults={this.state.numberOfResults}/>
                    <Pagination currentPage={this.state.pageData.currentPage} numberPages={this.state.pageData.numberPages}/>
                    <SearchResults resultsData={this.state.searchResultsData}/>
                </div>);
    }
}