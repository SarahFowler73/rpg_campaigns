import { combineReducers } from 'redux'
import { VisibilityFilters } from './actions'
const { SHOW_ALL } = VisibilityFilters

function visibilityFilter(state = SHOW_ALL, action) {
  switch (action.type) {
    case 'SET_VISIBILITY_FILTER':
      return action.filter
    default:
      return state
  }
}

function games(state = [], action) {
    console.log(state, action);
  switch (action.type) {
    case 'NEW_GAME':
      return [
        ...state,
        {
          title: action.title,
          description: action.description
        }
      ]
    case 'EDIT_GAME':
      return state.map((game, index) => {
        if (index === action.index) {
          return Object.assign({}, game, {
              title: action.title,
              description: action.description
          })
        }
        return game
      })
    default:
      return state
  }
}

export const gameListReducer = combineReducers({
  visibilityFilter,
  games
})
