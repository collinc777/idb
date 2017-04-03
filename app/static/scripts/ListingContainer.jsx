class ListingContainer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            cardData: props.listing_data
        }
    }

    render() {
        return (
                <div>
                    <TitleLayout/>
                    <SortAndFilterCards/>
                    <GridLayout data={this.state.cardData}/>
                </div>);
    }
}