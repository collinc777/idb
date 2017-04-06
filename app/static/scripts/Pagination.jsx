class PageLink extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            link: props.link,
            active: props.active,
            disabled: props.disabled
        }
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick(event){
        this.props.onChange(this.state.link);
        console.log("Changing page to: " + this.state.link); 
    }

    render() {
        // this.state.active + " " + this.state.disabled
        var classNameIfAny = "";
        if(this.state.active !== undefined){
            classNameIfAny += this.state.active + " ";
        }
        if(this.state.disabled !== undefined){
            classNameIfAny += this.state.disabled + " ";
        }

        return (
            <a className={classNameIfAny} href="#" onClick={this.handleClick}>{this.state.link}</a>
        )
    }
}

class Pagination extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            currentPage: 1,
            numberPages: props.numberPages
        }
        this.handleChange = this.handleChange.bind(this);
    }

    componentWillMount() {
        ajaxModel.updatePaginationCallback = (data) => {
            console.log("Updating pagination with: ", data);
            this.setState({currentPage: data["currentPage"], numberPages: data["numberPages"]});
        }
    }

    handleChange(page) {
        console.log(this);
        console.log("Page: ", page);
        if(page === "Previous"){
            this.setState({currentPage: this.state.currentPage - 1, numberPages: this.state.numberPages});
        }else if(page === "Next"){
            this.setState({currentPage: this.state.currentPage + 1, numberPages: this.state.numberPages});
        }else{
            this.setState({currentPage: page, numberPages: this.state.numberPages});
        }
        ajaxModel.setCurrentPage(page);
    }

    render() {
        console.log("Re-rendering Pagination");
        const totalPaginationLinks = 3;
        var paginationElements = [];

        var disabled = "disabled";
        var active = "active";
        var previous = "Previous";
        var next = "Next";

        var currentPage = this.state.currentPage;
        console.log("Rerendierng currentPAge: ", currentPage);
        var firstPage = Math.max(currentPage - 3, 1);
        var lastPage = Math.min(currentPage + 3, this.state.numberPages + 1);

        if(currentPage == 1){
            paginationElements.push(<PageLink key={Math.random(1, 999999)} link={previous} disabled={disabled} onChange={this.handleChange}/>);
        }else{
            paginationElements.push(<PageLink key={Math.random(1, 999999)} link={previous} onChange={this.handleChange}/>);
        }

        console.log("FirstPage: ", firstPage, " and lastPage: ", lastPage);

        for(var i = firstPage; i < lastPage; i++){
            (function(self, i){
                if(i == currentPage){
                    paginationElements.push(<PageLink key={Math.random(1, 999999)} link={i} active={active} onChange={self.handleChange}/>);
                }else{
                    paginationElements.push(<PageLink key={Math.random(1, 999999)} link={i} onChange={self.handleChange}/>);
                }
            })(this, i);
        }

        if(currentPage == this.state.numberPages){
            paginationElements.push(<PageLink key={Math.random(1, 999999)} link={next} disabled={disabled} onChange={this.handleChange}/>);
        }else{
            paginationElements.push(<PageLink key={Math.random(1, 999999)} link={next} onChange={this.handleChange}/>);
        }

        return (
                <div className="container paginationContainer text-center">
                    <div className="row pageLinks text-center">
                        {paginationElements}
                    </div>
                </div>
                
        );
    }
}