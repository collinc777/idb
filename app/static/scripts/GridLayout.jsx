class GridLayout extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            modelData: props.modelData
        }

    }

    componentWillMount() {
        ajaxModel.updateGridDataCallback = (modelData) => {
            if(modelData === undefined){
                window.alert("modelData is undefined!");
            }
            this.setState({modelData: modelData});
        }
    }

    /* Had to add a key= declaration to GridCard so that updates that had the 
       same number of rows actually prompted a re-rendering by React.js */

    render() {
        return (
                <div className="card-deck text-center">
                    {this.state.modelData.map((gc) => <GridCard key={Math.random(1,99999)} modelID={gc.id}
                                                           modelName={gc.name} modelURL={ajaxModel.modelURL}/>)}
                </div>
        );
    }
}