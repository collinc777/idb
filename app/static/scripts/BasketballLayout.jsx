//noinspection JSDuplicatedDeclaration
class TitleLayout extends React.Component {
    render() {
        return (
            <div>
                <h1>Basketball Mania Data Visualization</h1>
            </div>
        )
    }
}

class GameLayout extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: props.gameData
        }
    }

    render() {
        return (
            <div>
            </div>
        )
    }

}

class Chart extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: props.chartData,
            chartID: props.chartID,
            xAxis: props.xAxis,
            yAxis: props.yAxis
        }
    }

    render() {
        return (
            <div id={this.state.chartID}>

            </div>
        )
    }

    componentDidMount() {
        console.log("the egg");
        let actualData = this.state.data.players;
        let testArray = [];
        for (let i = 0; i < 100; i++) {
            testArray.push(actualData[i]);
        }
        let myData = [100, 125, 320, 440, 500, 250, 320, 720, 50];

        let margin = {top: 20, right: 30, bottom: 30, left: 40},
            width = 960 - margin.left - margin.right,
            height = 500 - margin.top - margin.bottom;

        let yScale = d3.scaleLinear()
            .range([height, 0])
            .domain([0, d3.max(testArray, function (d) {
                return d.PPG;
            })]);

        let xScale = d3.scaleBand()
            .rangeRound([0, width], .1)
            .domain(testArray.map(function (d) {
                console.log("the name is " + d.Name);
                return d.Name;
            }));

        let xAxis= d3.axisBottom(xScale);

        let yAxis = d3.axisLeft(yScale);


        // var colors = d3.scaleLinear()
        //     .domain([0, myData.length])
        //     .range(['#90ee90', '#30c230']);

        let myChart = d3.select('#' + this.state.chartID)
            .append('svg')
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        myChart.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
            .call(xAxis);

        myChart.append("g")
            .attr("class", "y axis")
            .call(yAxis);

        // let barWidth = width / testArray.length;

        myChart.selectAll(".bar")
            .data(testArray)
            .enter().append("rect")
            .attr("class", "bar")
            .attr("x", function (d) {
                return xScale(d.Name);
            })
            .attr("y", function (d) {
                return yScale(d.PPG);
            })
            .attr("height", function (d) {
                return height - yScale(d.PPG);
            })
            .attr("width", xScale.bandwidth());

        // bar.append("rect")
        //     .attr("y", function (d) {
        //         return yScale(d.PPG);
        //     })
        //     .attr("height", function (d) {
        //         return height - yScale(d.PPG);
        //     })
        //     .attr("width", xScale.bandwidth());
        //
        // bar.append("text")
        //     .attr("x", xScale.bandwidth() / 2)
        //     .attr("y", function (d) {
        //         return yScale(d.PPG) + 3;
        //     })
        //     .attr("dy", ".75em")
        //     .text(function (d) {
        //         return d.PPG;
        //     });

        function type(d) {
            d.PPG = +d.PPG; // coerce to number
            return d;
        }


    }


}

class PlayerLayout extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: props.playerData
        }
    }

    render() {
        console.log("the chicken");
        return (
            <Chart chartID="playerChart" chartData={this.state.data}/>
        )
    }
}


class TeamLayout extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: props.teamData
        }
    }

    render() {
        return (
            <div></div>
        )
    }

}

class VenueLayout extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: props.venueData
        }
    }

    render() {
        return (
            <div></div>
        )
    }
}


class BasketballContainer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            games: props.basketball_data.games,
            players: props.basketball_data.players,
            teams: props.basketball_data.teams,
            venues: props.basketball_data.venues,
        }
    }

    render() {
        return (
            <div>
                <TitleLayout title="Basketball Mania Data Visualization"/>
                <PlayerLayout playerData={this.state.players}/>
                <GameLayout gameData={this.state.games}/>
                <TeamLayout teamData={this.state.teams}/>
                <VenueLayout venuesData={this.state.venues}/>
            </div>
        )
    }
}

