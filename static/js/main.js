import React from 'react';
import {render} from 'react-dom';

console.log("This is main.js")

class App extends React.Component {
  render () {
    return <p> Hello World!</p>;
  }
}

render(<App/>, document.getElementById('app'));
