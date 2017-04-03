class GridCard extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            cardID: props.cardID,
            cardName: props.cardName,
            cardURL: props.cardURL
        }
    }

    render() {
        return (
                <div className="card listingCard">
                    <div className="card-header">
                        <h4><a href={this.state.cardURL + '/' + this.state.cardID}>{this.state.cardName}</a>
                        </h4>
                    </div>
                    <div className="card-block">
                        <a className="btn btn-block btn-default"
                           href={this.state.cardURL + '/' + this.state.cardID}>Details</a>
                    </div>
                </div>
        );
    }
}