// export const ADD_TODO = 'ADD_TODO'

// export const TOGGLE_TODO = 'TOGGLE_TODO'

// export const SET_VISIBILITY_FILTER = 'SET_VISIBILITY_FILTER'


/*
 * other constants
 */

export const VisibilityFilters = {
  SHOW_ALL: 'SHOW_ALL',
  SHOW_COMPLETED: 'SHOW_COMPLETED',
  SHOW_ACTIVE: 'SHOW_ACTIVE'
}

/*
 * action creators
 */

// export function addTodo(text) {
//   return { type: ADD_TODO, text }
// }
export function newGame(title, description) {
  return { type: 'NEW_GAME', title, description }
}


// export function toggleTodo(index) {
//   return { type: TOGGLE_TODO, index }
// }
export function editGame(title, description) {
  return { type: 'EDIT_GAME', title, description }
}


export function setVisibilityFilter(filter) {
  return { type: 'SET_VISIBILITY_FILTER', filter }
}
