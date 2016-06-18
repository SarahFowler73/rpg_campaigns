import React from 'react'
import  { render } from 'react-dom'
import { createStore } from 'redux'
import { Provider, connect } from 'react-redux'

import { gameListReducer } from './reducers'
import { GameForm, GameList} from './components'

let store = createStore(gameListReducer)

// const mapStateToProps = (state) => {
//   return {
//     // todos: getVisibleTodos(state.todos, state.visibilityFilter)
//     games: state.games
//   }
// }
//
// const mapDispatchToProps = (dispatch) => {
//   return {
//     onsubmit: () => {
//       dispatch({
//           type: 'NEW_GAME',
//           title: 'TEST',
//           description: 'TEST DESC'
//       })
//     }
//   }
// }
//todo: this isn't how you should dispatch shit
class GameListApp extends React.Component {
    render(){
        return(
        <div>
            <GameForm onsubmit={() => store.dispatch({
                type: 'NEW_GAME',
                title: 'TEST',
                description: 'TEST DESC'
            })}/>
            <GameList games={store.getState().games}/>
        </div>)
    }
}



// const JesusLetMeBeDone = connect(
//   mapStateToProps,
//   mapDispatchToProps
// )(GameListApp)


render(
    <Provider store={store}>
        <GameListApp />
    </Provider>,
    document.getElementById('app')
);
