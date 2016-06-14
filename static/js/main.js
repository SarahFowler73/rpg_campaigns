import React from 'react'
import  { render } from 'react-dom'
import { createStore } from 'redux'
import { Provider } from 'react-redux'

import { gameListReducer } from './reducers'
import { GameForm, GameList} from './components'

let store = createStore(gameListReducer)
// onClick=store.dispatch({
//     type: 'ADD_GAME',
//     title: 'TEST',
//     description: 'TEST DESC'
// })}

class GameListApp extends React.Component {
    render(){
        return(
        <div>
            <GameForm />
            <GameList games={[]}/>
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
