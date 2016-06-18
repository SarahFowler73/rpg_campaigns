import React, { PropTypes } from 'react';

export const GameForm = ({ onSubmit }) => {
    let gameObj = {};
    return (
        <div id='game-form'>
            <label>Title:
                <input type='text' name='game-title'
                    ref={node => {
                        gameObj.title = node;
                }}/>
            </label>
            <label>Description:
                <textarea name='game-description'
                    ref={node => {
                        gameObj.description = node;
                }}/>
            </label>
            <button className="thing" onClick={() => onSubmit(gameObj)}>
                Save Changes
            </button>
        </div>
    )
}

GameForm.propTypes = {
  onSubmit: PropTypes.func.isRequired
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
