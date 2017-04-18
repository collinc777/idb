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
            data: props.gameData.games
        }
    }

    render() {
        return (
            <div id="gameChart">
            </div>
        )
    }

    componentDidMount() {
        let games = this.state.data;
        let teamsWins = {};
        for (let i = 0; i < games.length; i++) {
            let winningTeam = games[i]["Winning Team"];
            let gamesWon = teamsWins[winningTeam];
            if (gamesWon == null) {
                gamesWon = 0;
            }
            gamesWon = gamesWon + 1;
            teamsWins[winningTeam] = gamesWon
        }
        let teamWinsArray = [];
        for (let team in teamsWins) {
            let teamObject = {};
            teamObject.name = team;
            teamObject.wins = teamsWins[team];
            teamWinsArray.push(teamObject);
        }

        let margin = {top: 20, right: 30, bottom: 100, left: 40},
            width = 960 - margin.left - margin.right,
            height = 500 - margin.top - margin.bottom;

        let yScale = d3.scaleLinear()
            .range([height, 0])
            .domain([0, d3.max(teamWinsArray, function (d) {
                return d.wins;
            })]);
        let xScale = d3.scaleBand()
            .rangeRound([0, width], .1)
            .domain(teamWinsArray.map(function (d) {
                return d.name;
            }));
        let xAxis = d3.axisBottom(xScale);

        let yAxis = d3.axisLeft(yScale);

        let myChart = d3.select('#playerChart')
            .append('svg')
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        myChart.append("g")
            .attr("class", "y axis")
            .call(yAxis)
            .append("text")
            .attr("transform", "rotate(-91)")
            .attr("y", 6)
            .attr("dy", ".71em")
            .style("text-anchor", "end")
            .style("fill", "white")
            .style("font-size", 15)
            .text("Games Won");

        myChart.selectAll(".bar")
            .data(teamWinsArray)
            .enter().append("rect")
            .attr("class", "bar")
            .attr("x", function (d) {
                return xScale(d.name);
            })
            .attr("y", function (d) {
                return yScale(d.wins);
            })
            .attr("height", function (d) {
                return height - yScale(d.wins);
            })
            .attr("width", xScale.bandwidth());

        myChart.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
            .call(xAxis)
            .selectAll("text")
            .attr("y", 0)
            .attr("x", 9)
            .attr("dy", ".35em")
            .attr("transform", "rotate(90)")
            .style("text-anchor", "start")
            .style("fill", "white");

        myChart.append("text")
            .attr("x", (width / 2))
            .attr("y", 10 - (margin.top / 2))
            .attr("text-anchor", "middle")
            .style("font-size", "16px")
            .style("text-decoration", "underline")
            .style("fill", "white")
            .text("Games Won Per Team");

        function type(d) {
            d.wins = +d.wins; // coerce to number
            return d;
        }
    }

}

class PlayerLayout extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: props.playerData.players
        }
    }

    render() {
        console.log("the chicken");
        return (
            <div id="playerChart"></div>
        )
    }

    componentDidMount() {
        console.log("the egg");
        let actualData = this.state.data;
        actualData.sort(function (a, b) {
            return b.PPG - a.PPG;
        });
        let testArray = [];
        for (let i = 0; i < 100; i++) {
            testArray.push(actualData[i]);
        }
        console.log(type(actualData));

        let margin = {top: 20, right: 30, bottom: 100, left: 40},
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
                return d.Name;
            }));

        let xAxis = d3.axisBottom(xScale);

        let yAxis = d3.axisLeft(yScale);


        // var colors = d3.scaleLinear()
        //     .domain([0, myData.length])
        //     .range(['#90ee90', '#30c230']);

        let myChart = d3.select('#playerChart')
            .append('svg')
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        // myChart.append("g")
        //     .attr("class", "x axis")
        //     .attr("transform", "translate(0," + height + ")")
        //     .call(xAxis);

        myChart.append("g")
            .attr("class", "y axis")
            .call(yAxis)
            .append("text")
            .attr("transform", "rotate(-91)")
            .attr("y", 6)
            .attr("dy", ".71em")
            .style("text-anchor", "end")
            .style("fill", "black")
            .style("font-size", 15)
            .text("Points Per Game");

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

        myChart.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
            .call(xAxis)
            .selectAll("text")
            .attr("y", 0)
            .attr("x", 9)
            .attr("dy", ".35em")
            .attr("transform", "rotate(90)")
            .style("text-anchor", "start");

        myChart.append("text")
            .attr("x", (width / 2))
            .attr("y", 10 - (margin.top / 2))
            .attr("text-anchor", "middle")
            .style("font-size", "16px")
            .style("text-decoration", "underline")
            .text("Top Scoring players PPG");

        function type(d) {
            d.PPG = +d.PPG; // coerce to number
            return d;
        }
    }
}


class TeamLayout extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: props.teamData.teams
        }
    }

    render() {
        return (
            <div id="teamChart"></div>
        )
    }

    componentDidMount() {
        let teams = this.state.data;

        let margin = {top: 20, right: 30, bottom: 100, left: 40},
            width = 960 - margin.left - margin.right,
            height = 500 - margin.top - margin.bottom;

        let yScale = d3.scaleLinear()
            .range([height, 0])
            .domain([0, d3.max(teams, function (d) {
                return d.PPG;
            })]);
        let xScale = d3.scaleBand()
            .rangeRound([0, width], .1)
            .domain(teams.map(function (d) {
                return d.Name;
            }));
        let xAxis = d3.axisBottom(xScale);

        let yAxis = d3.axisLeft(yScale);

        let myChart = d3.select('#playerChart')
            .append('svg')
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        myChart.append("g")
            .attr("class", "y axis")
            .call(yAxis)
            .append("text")
            .attr("transform", "rotate(-91)")
            .attr("y", 6)
            .attr("dy", ".71em")
            .style("text-anchor", "end")
            .style("fill", "white")
            .style("font-size", 15)
            .text("PPG");

        myChart.selectAll(".bar")
            .data(teams)
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

        myChart.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
            .call(xAxis)
            .selectAll("text")
            .attr("y", 0)
            .attr("x", 9)
            .attr("dy", ".35em")
            .attr("transform", "rotate(90)")
            .style("text-anchor", "start")
            .style("fill", "white");
        myChart.append("text")
            .attr("x", (width / 2))
            .attr("y", 10 - (margin.top / 2))
            .attr("text-anchor", "middle")
            .style("font-size", "16px")
            .style("text-decoration", "underline")
            .style("fill", "white")
            .text("Avg Points scored per team");

        function type(d) {
            d.wins = +d.wins; // coerce to number
            return d;
        }
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

