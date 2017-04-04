class TitleLayout extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            title: props.title
        }
    }

    render() {
        return (<div className="text-center">
            <h1 className="cursive">{this.state.title}</h1>
            <br/>
        </div>);
    }
}

class ListingContainer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            listingTitle: props.listing_title,
            cardData: props.listing_data
        }
    }

    render() {
        return (
                <div>
                    <TitleLayout title={this.state.listingTitle}/>
                    <SortAndFilterCards/>
                    <GridLayout data={this.state.cardData}/>
                </div>);
    }
}