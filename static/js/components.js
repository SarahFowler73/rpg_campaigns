import React, { PropTypes } from 'react';

export const GameForm = ({ onsubmit }) => (
    <div id='game-form'>
        <label>Title:
            <input type='text' name='game-title'/>
        </label>
        <label>Description:
            <textarea name='game-description'/>
        </label>
        <button className="thing" onClick={onsubmit}>Save Changes</button>
    </div>
)

GameForm.propTypes = {
  onsubmit: PropTypes.func.isRequired
}

export const GameList = ({ games }) => (
    <ul className="games">
        {games.map(game =>
            <li key={game.id}>
                <h4>{game.title}</h4>
                <p>{game.description}</p>
                <button>Edit</button>
            </li>
        )}
    </ul>
)

GameList.propTypes = {
  games: PropTypes.array.isRequired
}
