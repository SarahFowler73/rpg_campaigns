import React from 'react';
import  ReactDOM from 'react-dom';
import {createStore} from 'redux';

import {GameList} from './makeEditGame';

let R = React.DOM;

// class App extends React.Component {
// var App = React.createClass ({
    // get: function() {
    //     $.ajax({
    //         url: this.props.getUrl,
    //         datatype: 'json',
    //         cache: false,
    //         success: function(data) {
    //             this.setState({data: data.results});
    //         }.bind(this)
    //     })
    // },
    //
    // post: function(postData) {
    //     $.ajax({
    //         url: this.props.postUrl,
    //         dataType: 'json',
    //         type: 'POST',
    //         data: postData,
    //         success: function(data) {
    //             this.setState({data: data});
    //         }.bind(this),
    //         error: function(xhr, status, err) {
    //             console.error(this.props.postUrl, status, err.toString());
    //         }.bind(this)
    //     });
    // },


    // getInitialState: function() {
    //     return {data: []};
    // },

    // componentDidMount: function() {
    //     this.get();
    // },
//     render: function() {
//         if (this.state.data) {
//             console.log('DATA!', this.state.data)
//             var gameNodes = this.state.data.map(
//                 (game) => {
//                     return R.ul({key: game.id},
//                         R.li(null, game.title),
//                         R.li(null, game.creation_date)
//                     )
//                 }
//             )
//         }
//         return (
//             R.div(null,
//                 R.h1(null, 'Hello React without JSX!'),
//                 gameNodes
//             )
//         )
//     }
// })


ReactDOM.render(
    // React.createElement(App, {getUrl: '/api/v1/campaigns/game/'}),
    React.createElement(GameList),
    document.getElementById('app')
);
