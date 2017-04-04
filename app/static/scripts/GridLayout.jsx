class GridLayout extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: props.data
        }

    }

    componentWillMount() {
        console.log("Mounting gridlayout");
        ajaxModel.updateGridDataCallback = (data) => {
            this.setState({data: data});
        }
    }

    render() {
        return (
                <div className="card-deck text-center">
                    {this.state.data.map((gc) => <GridCard cardID={gc.cardID}
                                                           cardName={gc.cardName} cardURL={gc.cardURL}/>)}
                </div>
        );
    }
}