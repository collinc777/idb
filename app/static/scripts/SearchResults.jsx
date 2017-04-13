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

    render() {
        return (
                <div className="container searchResultsContainer text-center">
                	{this.state.resultsData.map((sr) => <SearchResultCard key={Math.random(1, 999999)} resultID={sr.resultID} resultModelName={sr.resultModelName} resultModelType={sr.resultModelType} resultDetails={sr.resultDetails} />)}    
                </div>);
    }
}