import React from 'react';
import  ReactDOM from 'react-dom';

console.log("This is main.js")

// class App extends React.Component {
var App = React.createClass ({
    loadGamesFromServer: function() {
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data.results});
            }.bind(this)
        })
    },

    getInitialState: function() {
        return {data: []};
    },

    componentDidMount: function() {
        this.loadGamesFromServer();
        // setInterval(this.loadGamesFromServer,
        //             this.props.pollInterval)
    },
    render: function() {
        if (this.state.data) {
            console.log('DATA!', this.state.data)
            var gameNodes = this.state.data.map(
                (game) => {
                    return <li key={game.id}>
                        <ul>
                            <li>{game.title}</li>
                            <li>{game.creation_date}</li>
                        </ul>
                    </li>
                }
            )
        }
        return (
            <div>
                <h1>Hello React!</h1>
                <ul>
                    {gameNodes}
                </ul>
            </div>
        )
    }
})

//   render () {
//     return <p> Hello World!</p>;
//   }
// }

ReactDOM.render(
    <App url='/api/v1/campaigns/game/'/>,
    document.getElementById('app')
);
