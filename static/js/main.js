import React from 'react'
import  { render } from 'react-dom'
import { createStore } from 'redux'
import { Provider } from 'react-redux'

import { gameListReducer } from './reducers'
import { gameForm, gameList} from './components'

let store = createStore(gameListReducer)

const newGameOnclick = store.dispatch({
    type: 'ADD_GAME',
    title: 'TEST',
    description: 'TEST DESC'
});

class GameListApp extends React.Component {
    render(){
        return(
        <div>
            <gameForm onclick={newGameOnclick}/>
            <gameList props={store.getState().games}/>
            <p>Something is here!</p>
        </div>)
    }

}

render(
    <Provider store={store}>
        <GameListApp />
    </Provider>,
    document.getElementById('app')
);


store.subscribe(render);
