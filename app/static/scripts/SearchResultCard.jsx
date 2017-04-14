class SearchResultCard extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            resultID: props.resultID,
            resultModelName: props.resultModelName,
            resultModelType: props.resultModelType,
            resultDetails: props.resultDetails
        }
    }

    render() {
        var typeCapitalized = this.state.resultModelType.charAt(0).toUpperCase() + this.state.resultModelType.slice(1);
        var innerHTML = {__html: this.state.resultDetails};
        return (
                <div className="card searchResultCard">
                    <div className="card-header">
                        <h4><a href={'/' + this.state.resultModelType + 's/' + this.state.resultID}>| {typeCapitalized} | {this.state.resultModelName}</a>
                        </h4>
                    </div>
                    <div dangerouslySetInnerHTML={innerHTML} className="card-block">
                    </div>
                </div>
        );
    }
}