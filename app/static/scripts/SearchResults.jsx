class SearchResults extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            resultsData: props.resultsData
        }
    }

    componentWillMount() {
        ajaxModel.updateResultsDataCallback = (data) => {
            this.setState({resultsData: data});
        }
    }

    componentDidMount(){
        // Called only on page 1
        ajaxModel.highlightPropertyMatches();
    }

    componentDidUpdate() {
        // Called when pages update
        ajaxModel.highlightPropertyMatches();
    }

    render() {
        return (
                <div className="container searchResultsContainer text-center">
                	{this.state.resultsData.map((sr) => 
                        <SearchResultCard key={Math.random(1, 999999)} resultID={sr.resultID} resultModelName={sr.resultModelName} resultModelType={sr.resultModelType} resultPropertyMatches={sr.resultPropertyMatches} />
                    )}    
                </div>);
    }
}