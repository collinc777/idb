class DetailsContainer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
        	detailsName: props.details_name,
        	detailsImageLink: props.details_image_link,
            detailsData: props.details_data
        }
    }

    componentDidMount(){
    	// Wait 300 milliseconds then scroll to the selected property
    	window.setTimeout(function(){
    		ajaxModel.scrollToSelectedProperty(window.location.hash);
    	}, 300);
    }
	
    render() {
        return (
                <div className="details">
                	<ImageAndNameCard name={this.state.detailsName} imageLink={this.state.detailsImageLink} />
                    {this.state.detailsData.map((dc) => 
                    	<DetailsCard key={Math.random(1,99999)} readableName={dc.readableName} propertyName={dc.propertyName} propertyType={dc.propertyType}
                    	propertyValue={dc.propertyValue} propertyModelLinks={dc.propertyModelLinks} />)}
	            </div>
        );
    }
}