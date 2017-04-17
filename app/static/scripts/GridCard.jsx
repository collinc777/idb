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
        var imageURL = ajaxModel.getImageURL(this.state.modelURL, this.state.modelID);
        return (
                <div className="card listingCard">
                    <div className="card-header">
                        <h4><a href={this.state.modelURL + '/' + this.state.modelID}>{this.state.modelName}</a>
                        </h4>
                    </div>
                    <img className="card-img-bottom" src={imageURL}></img>

                </div>
        );
    }
}