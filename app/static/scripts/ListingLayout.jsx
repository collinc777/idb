class TitleLayout extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            title: props.title
        }
    }

    render() {
        return (<div className="text-center">
            <h1 className="cursive listingTitle">{this.state.title}</h1>
            <br/>
        </div>);
    }
}

class ListingContainer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            listingTitle: props.listing_title,
            cardData: props.listing_card_data,
            pageData: props.listing_page_data,
            sorts: props.listing_sorts,
            filterPlaceholder: props.listing_filter_placeholder
        }
    }

    render() {
        return (
                <div>
                    <TitleLayout title={this.state.listingTitle}/>
                    <SortAndFilterCards sorts={this.state.sorts} filterPlaceholder={this.state.filterPlaceholder}/>
                    <Pagination currentPage={this.state.pageData.currentPage} numberPages={this.state.pageData.numberPages}/>
                    <GridLayout data={this.state.cardData}/>
                </div>);
    }
}