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
    render() {
        return (
            <div className="chart">
                <div style={{width: 40}}>4</div>
                <div style={{width: 80}}>8</div>
                <div style={{width: 150}}>15</div>
                <div style={{width: 160}}>16</div>
                <div style={{width: 230}}>230</div>
                <div style={{width: 420}}>420</div>
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

    render() {
        return (
            <div>
                <Chart />
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

