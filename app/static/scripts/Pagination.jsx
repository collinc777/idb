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

        var onClick = this.handleClick;
        if(this.state.disabled !== undefined){
            onClick="";
        }

        return (
            <a className={classNameIfAny} href="#" onClick={onClick}>{this.state.link}</a>
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
        ajaxModel.updatePaginationCallback = (pageData) => {
            console.log("Updating pagination with: ", pageData);
            this.setState({currentPage: pageData["currentPage"], numberPages: pageData["numberPages"]});
        }
    }

    handleChange(page) {
        if(page === "Previous"){
            page = this.state.currentPage - 1;
        }else if(page === "Next"){
            page = this.state.currentPage + 1;
        }
        this.setState({currentPage: page, numberPages: this.state.numberPages});
        ajaxModel.setCurrentPage(page);
    }

    render() {
        console.log("Re-rendering Pagination");
        var currentPage = this.state.currentPage;
        var totalPaginationLinks = Math.min(this.state.numberPages, 7);
        var paginationElements = [];

        var disabled = "disabled";
        var active = "active ";
        var previous = "Previous";
        var next = "Next";

        console.log("Rerendering currentPage: ", currentPage);
        var firstPage = Math.max(currentPage - 3, 1);
        if(firstPage + 6 > this.state.numberPages){
            firstPage = Math.max(this.state.numberPages - 6, 1);
        }

        if(currentPage == 1){
            paginationElements.push(<PageLink key={Math.random(1, 999999)} link={previous} disabled={disabled}/>);
        }else{
            paginationElements.push(<PageLink key={Math.random(1, 999999)} link={previous} onChange={this.handleChange}/>);
        }

        var i = firstPage;
        while(totalPaginationLinks > 0){
            (function(self, i){
                if(i == currentPage){
                    paginationElements.push(<PageLink key={Math.random(1, 999999)} link={i} active={active} onChange={self.handleChange}/>);
                }else{
                    paginationElements.push(<PageLink key={Math.random(1, 999999)} link={i} onChange={self.handleChange}/>);
                }
            })(this, i);
            totalPaginationLinks--;
            i++;
        }

        if(currentPage == this.state.numberPages){
            paginationElements.push(<PageLink key={Math.random(1, 999999)} link={next} disabled={disabled}/>);
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