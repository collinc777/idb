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
        var actualData = this.state.data;
        var myData = [100, 125, 320, 440, 500, 250, 320, 720, 50];

        var margin = {
            top: 30,
            right: 30,
            bottom: 40,
            left: 50
        }
        var height = 500 - margin.top - margin.bottom;
        var width = 500 - margin.right - margin.left;
        var animateDuration = 700;
        var animateDelay = 30;
        // var barWidth = 35;
        // var barOffset = 5;
        var tooltip = d3.select('body').append('div')
            .style('position', 'absolute')
            .style('background', '#f4f4f4')
            .style('padding', '5 15px')
            .style('border', '1px #333 solid')
            .style('border-radius', '5px')
            .style('opacity', '0');

        var yScale = d3.scaleLinear()
            .domain([0, d3.max(myData)])
            .range([0, height]);

        var xScale = d3.scaleBand()
            .domain(d3.range(0, myData.length))
            .range([0, width]);

        var colors = d3.scaleLinear()
            .domain([0, myData.length])
            .range(['#90ee90', '#30c230']);

        var myChart = d3.select('#' + this.state.chartID)
            .append('svg')
            .attr('width', width + margin.right + margin.left)
            .attr('height', height + margin.top + margin.bottom)
            .append('g')
            .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')')
            .style('background', '#f4f4f4')
            .selectAll('rect')
            .data(myData)
            .enter().append('rect')
            .style('fill', function (d, i) {
                return colors(i);
            })
            .attr('width', xScale.bandwidth())
            .attr('height', 0)
            .attr('x', function (d, i) {
                return xScale(i);

            })
            .attr('y', height)
            .on('mouseover',
                function (d) {
                    tooltip.transition()
                        .style('opacity', 1)

                    tooltip.html(d)
                        .style('left', (d3.event.pageX) + 'px')
                        .style('top', (d3.event.pageY + 'px'))
                    d3.select(this).style('opacity', .5);
                })
            .on('mouseout', function (d) {
                tooltip.transition()
                    .style('opacity', 0)
                d3.select(this).style('opacity', 1);
            })

        myChart.transition()
            .attr('height', function (d) {
                return yScale(d);
            })
            .attr('y', function (d) {
                return height - yScale(d);
            })
            .duration(animateDuration)
            .delay(function (d, i) {
                return i * animateDelay
            })
            .ease(d3.easeElastic);

        var vScale = d3.scaleLinear()
            .domain([0, d3.max(myData)])
            .range([height, 0]);

        var hScale = d3.scaleBand()
            .domain(d3.range(0, myData.length))
            .range([0, width]);

        var vAxis = d3.axisLeft(vScale)
            .ticks(5)
            .tickPadding(5)

        var vGuide = d3.select('svg')
            .append('g')
        vAxis(vGuide)
        vGuide.attr('transform', 'translate(' + margin.left + ', ' + margin.top + ')')
        vGuide.selectAll('path')
            .style('fill', 'none')
            .style('stroke', '#000')
        vGuide.selectAll('line')
            .style('stroke', '#000')

        var hAxis = d3.axisBottom(hScale)
            .tickValues(hScale.domain().filter(function (d, i) {
                return !(i % (myData.length / 5));
            }));

        var hGuide = d3.select('svg')
            .append('g')
        hAxis(hGuide)
        hGuide.attr('transform', 'translate(' + margin.left + ',' + (height + margin.top) + ')')
        hGuide.selectAll('path')
            .style('fill', 'none')
            .style('stroke', '#000')
        hGuide.selectAll('line')
            .style('stroke', '#000')

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

