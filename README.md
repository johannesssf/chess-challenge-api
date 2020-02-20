# Chess challenge RESTful API

The project consists of a simplified REST API which allows the user to register pieces into a chess board.

## Registering
The information used to register are name and color.

**The piece name must be one of:**
* king
* queen
* rook
* bishop
* knight
* pawn

**And the piece color one of:**
* black
* white

Example:

    POST <app-url>/addpiece
    {
        "name": "knight",
        "color": "white"
    }

    Response
    {
	    "piece_id": "KnW2"
    }

## Retrieving
It's also possible to get information about a registered piece. To do that it's necessary to use the *piece_id* returned when a piece is registered and the chessboard coordinate (algebraic notation). However, if the piece being consulted is a **Knight** the API will calculate all possible locations where the knight can move within 2 turns, based on the given location. Otherwise, no moves will be calculated.

Example:

    GET <app-url>/piece
    {
        "coord": "1E",
        "piece_id": "KnW2"
    }

    Response
    {
        "piece_id": "KnW2",
        "coord": "1E",
        "possible_moves": {
        "first_turn": ["3F",  "3D", "2G", "2C"],
        "second_turn": {
            "3F": ["1G", "1E", "5G", "5E", "4H", "2H", "4D", "2D"],
            "3D": ["1E", "1C", "5E", "5C", "4F", "2F", "4B", "2B"],
            "2G": ["4H", "4F", "3E", "1E"],
            "2C": ["4D", "4B", "3E", "1E", "3A", "1A"]
        }}
    }

## Testing
The file *chess-challenge-api.postman_collection.json* can be used to execute tests the postman application.
