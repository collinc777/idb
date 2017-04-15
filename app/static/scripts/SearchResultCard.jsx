class ResultPropertyMatch extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            resultURL: props.resultURL,
            propertyName: props.propertyName,
            propertyReadable: props.propertyReadable,
            propertyValue: props.propertyValue
        }
    }

    render() {
        return (
                <div className="row resultPropertyMatchRow" data-url={this.state.resultURL + "#" + this.state.propertyName}>
                    <div className="col-md-3 col-xs-12">
                        <h5>{this.state.propertyReadable}</h5>
                    </div>
                    <div className="col-md-9 col-xs-12 resultPropertyMatchValue">
                        {this.state.propertyValue}
                    </div>
                </div>
        );
    }
}

class SearchResultCard extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            resultID: props.resultID,
            resultModelName: props.resultModelName,
            resultModelType: props.resultModelType,
            resultPropertyMatches: props.resultPropertyMatches
        }
    }

    render() {
        var typeCapitalized = this.state.resultModelType.charAt(0).toUpperCase() + this.state.resultModelType.slice(1);
        var resultURL = '/' + this.state.resultModelType + 's/' + this.state.resultID;
        return (
                <div className="card searchResultCard">
                    <div className="card-header">
                        <h4><a href={resultURL}>| {typeCapitalized} | {this.state.resultModelName}</a>
                        </h4>
                    </div>
                    <div className="card-block">
                        <div className="container-fluid">
                            {this.state.resultPropertyMatches.map((rpm) => <ResultPropertyMatch key={Math.random(1, 999999)} propertyName={rpm.propertyName} propertyReadable={rpm.propertyReadable} propertyValue={rpm.propertyValue} resultURL={resultURL} />)} 
                        </div>
                    </div>
                </div>
        );
    }
}