class FilterCard extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            value: ""
        };
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event){
        this.setState({
            value: event.target.value
        });
        ajaxModel.filterData(event.target.value);
    }

    render() {
        return (<div className="card sortAndFilterCard text-center">
            <h3 className="card-header">Filter By</h3>
            <div className="card-block">
                <input type="text" className="form-control form-control-lg" placeholder={this.props.placeholder} value={this.state.value} onChange={this.handleChange}></input>
            </div>
        </div>);
    }

}

class SortCard extends React.Component {
    constructor(props) {
        super(props);
        console.log(props.sorts);
        this.state = {
            sorts: props.sorts,
            selectedSortName: props.sorts[0][1] + " Ascending",
            selectedSort: 0,
            ascending: 1
        }
        this
    }

    getSortName(selectedSort, ascending){
        var name = this.props.sorts[selectedSort][1];
        if(ascending === 0){
            name += " Descending";
        }else{
            name += " Ascending";
        }
        return name;
    }

    onSortData(selectedSort, ascending){
        var sort = this.props.sorts[selectedSort][0];
        var sortName = this.getSortName(selectedSort, ascending);
        this.setState({
            selectedSortName: sortName,
            selectedSort: selectedSort,
            ascending: ascending
        });
        ajaxModel.sortData(sort, ascending);
    }

    render() {
        /*
            The next for loop was the only way I could find to render a list
            of html elements. The weird (function(){})(); syntax is a closure
            to trap the i variable's value so that it doesn't just use the 
            final value for EVERY <a> tag. 
        */ 
        var sortsElements = [];
        for(var i = 0; i < this.props.sorts.length; i++){
            (function(sortCardInstance, i){
                var sort = sortCardInstance.props.sorts[i][1];
                sortsElements.push(<a key={Math.random(0, 999999)} className="dropdown-item" href="#" onClick onClick={() => sortCardInstance.onSortData(i, 1)}>{sort} Ascending</a>);
                sortsElements.push(<a key={Math.random(0, 999999)} className="dropdown-item" href="#" onClick onClick={() => sortCardInstance.onSortData(i, 0)}>{sort} Descending</a>);
            })(this, i);
        }
        return (<div className="card sortAndFilterCard text-center">
            <h3 className="card-header">Sort By</h3>
            <div className="card-block">
                <div className="dropdown">
                    <button className="btn btn-block btn-lg btn-secondary dropdown-toggle"
                            type="button"
                            id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true"
                            aria-expanded="false">
                        {this.state.selectedSortName}
                    </button>
                    <div className="dropdown-menu" aria-labelledby="dropdownMenuButton">
                        {sortsElements}
                    </div>
                </div>
            </div>
        </div>);
    }
}
class SortAndFilterCards extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            sorts: props.sorts,
            filterPlaceholder: props.filterPlaceholder
        }

    }

    render() {
        return (
                <div className="card-group">
                    <SortCard sorts={this.state.sorts}/>
                    <FilterCard placeholder={this.state.filterPlaceholder}/>
                </div>

        );
    }
}