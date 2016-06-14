import React from 'react';

const R = React.DOM;

export function GameTitle(props) {
    return (
        R.form({id: 'game-form', action: '/'},
            R.label({'for': 'game-title'}, 'Title: '),
            R.input({type: 'text', name: 'game-title'})
            R.label({'for': 'game-description'}, 'Description: ')
            R.textbox({name: 'game-description'})
        )
    )
}

export function GameList(props) {
    return (
        R.div({id: 'game-list'},
            React.createElement(GameTitle),
            R.ul({className: 'games'},
                R.li(null, 'Game Name',
                    R.button(null, 'Edit')
                )
            )
        )
    )
}
