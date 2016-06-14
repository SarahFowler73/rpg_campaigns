import React from 'react';

export default function gameForm(onclick) {
    return
        (<form id='game-form' action='/'>
            <label>Title:
                <input type='text' name='game-title'/>
            </label>
            <label>Description:
                <textbox name='game-description'/>
            </label>
            <button onClick={onclick}>Save Changes</button>
        </form>)
}

export default function gameList(props) {
    return
        (<ul className="games">
            {props.games.map(game =>
                <li key={game.id}>
                    <h4>{game.title}</h4>
                    <p>{game.description}</p>
                    <button>Edit</button>
                </li>
            )}
        </ul>)
}
