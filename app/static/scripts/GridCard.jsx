class GridCard extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            modelID: props.modelID,
            modelName: props.modelName,
            modelURL: props.modelURL
        }
    }

    render() {
        return (
                <div className="card listingCard">
                    <div className="card-header">
                        <h4><a href={this.state.modelURL + '/' + this.state.modelID}>{this.state.modelName}</a>
                        </h4>
                    </div>
                    <div className="card-block">
                        <a className="btn btn-block btn-default"
                           href={this.state.modelURL + '/' + this.state.modelID}>Details</a>
                    </div>
                </div>
        );
    }
}