class FilterCard extends React.Component {
    render() {
        return (<div className="card text-center">
            <h3 className="card-header">Filter By</h3>
            <div className="card-block">
                <input type="text" className="form-control form-control-lg" placeholder="Name..."></input>
            </div>
        </div>);
    }

}

class SortCard extends React.Component {
    constructor(props) {
        super(props);
    }

    onSortData(field, ascending){
        ajaxModel.sortData(field, ascending);
    }

    render() {
        return (<div className="card text-center">
            <h3 className="card-header">Sort By</h3>
            <div className="card-block">
                <div className="dropdown">
                    <button className="btn btn-block btn-lg btn-secondary dropdown-toggle"
                            type="button"
                            id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true"
                            aria-expanded="false">
                        Sort By
                    </button>
                    <div className="dropdown-menu" aria-labelledby="dropdownMenuButton">
                        <a className="dropdown-item" href="#" onClick={() => this.onSortData("cardName", 1)}>Name
                            Ascending</a>
                        <a className="dropdown-item" href="#" onClick={() => this.onSortData("cardName", 0)}>Name
                            Descending</a>
                        <a className="dropdown-item" href="#" onClick={() => this.onSortData("cardID", 1)}>ID Ascending</a>
                        <a className="dropdown-item" href="#" onClick={() => this.onSortData("cardID", 0)}>ID Descending</a>
                    </div>
                </div>
            </div>
        </div>);
    }
}
class SortAndFilterCards extends React.Component {
    constructor(props){
        super(props);

    }

    render() {
        return (
                <div className="card-group">
                    <SortCard/>
                    <FilterCard/>
                </div>

        );
    }
}