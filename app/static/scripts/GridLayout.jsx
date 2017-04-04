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

    /* Had to add a key= declaration to GridCard so that updates that had the 
       same number of rows actually prompted a re-rendering by React.js */

    render() {
        return (
                <div className="card-deck text-center">
                    {this.state.data.map((gc) => <GridCard key={gc.cardID} cardID={gc.cardID}
                                                           cardName={gc.cardName} cardURL={gc.cardURL}/>)}
                </div>
        );
    }
}