class ImageAndNameCard extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            name: props.name,
            imageLink: props.imageLink
        }
    }

    render() {

        return (
                <div id="name" className="card text-center">
                    <div className="card-header text-center">
                        <h1 className="cursive">{this.state.name}</h1>
                    </div>
                    <div className="card-block text-center">
                        <img className="detailsImage" src={this.state.imageLink} />
                    </div>
                </div>
        );
    }
}

class DetailsCard extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            readableName: props.readableName,
            propertyName: props.propertyName,
            propertyType: props.propertyType,
            propertyValue: props.propertyValue,
            propertyModelLinks: props.propertyModelLinks
        }
    }

    render() {
        /*
            propertyType possible values: 
            "linkarray": combines the next two, value will be array of ids, modelLinks will have links to the models
            "link": link to another model, value will be ID, modelLinks will have links to the models
            "array": array of elements, value will be array
            "default": just display readable name and then the value in text
        */
        var displayValue = this.state.propertyValue;

        switch(this.state.propertyType){
            case "link":
                var modelLink = ajaxModel.getModelLink(this.state.propertyModelLinks, displayValue);
                displayValue = (<div className="col-xs-12 col-md-6 text-center"><a href={modelLink["url"]}>{modelLink["name"]}</a></div>);

                break;
            case "array":
                var items = [];
                for(var i = 0; i < displayValue.length; i++){
                    items.push(
                        (function(itemText){
                            return (<div className="col-xs-12 col-md-6 text-center" key={Math.random(0, 99999)}>{itemText}</div>);
                        })(displayValue[i])
                    );
                }
                displayValue = (<div className="row">{items}</div>);            
                break;
            case "linkarray":
                var items = [];

                for(var i = 0; i < displayValue.length; i++){
                    items.push(
                        (function(modelLinks, item){
                            var modelLink = ajaxModel.getModelLink(modelLinks, item);
                            return (<div className="col-xs-12 col-md-6 text-center" key={Math.random(0, 99999)}><a href={modelLink["url"]}>{modelLink["name"]}</a></div>);
                        })(this.state.propertyModelLinks, displayValue[i])
                    );
                    
                }
                displayValue = (<div className="row">{items}</div>);
                
                break;
            case "default":
                displayValue = (<div className="detailValue">{displayValue}</div>);
                break;
            default:
                displayValue = (<div className="detailValue">{displayValue}</div>);
                console.log("Property Type: " + this.state.propertyType + " not implemened");
        }
        

        return (
                <div id={this.state.propertyName} className="card">
                    <h4 className="card-header text-center">{this.state.readableName}</h4>
                    <div className="card-block">
                        <div className="container-fluid">
                            {displayValue}
                        </div>
                    </div>
                </div>
        );
    }
}
