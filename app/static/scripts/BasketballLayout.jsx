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
    }

    render() {
        return (
            <div>

            </div>
        )
    }
}

class PlayerLayout extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: props.playerData
        }
    }

    componentDidMount() {
        console.log("the egg");

        var myData = [100, 125, 320, 440, 500];
        var height = 500;
        var width = 500;
        var barWidth = 35;
        var barOffset = 5;

        var myChart = d3.select('#chart').append('svg').attr('width', width)
            .attr('height', height)
            .style('background', '#f4f4f4')
            .selectAll('rect')
            .data(myData)
            .enter().append('rect')
            .style('fill', 'green')
            .attr('width', barWidth)
            .attr('height', function (d) {
                return d;
            })
            .attr('x', function (d, i) {
                return i * (barWidth + barOffset);

            })
            .attr('y', function (d) {
                return height - d;
            })
    }

    render() {
        console.log("the chicken");
        return (
            <div id="chart">
            </div>
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

