"""Chess board
"""


class PieceNotFoundError(Exception):
    pass


class BoardModel:

    def __init__(self):
        """Creates a new board.
        """
        self.board_pieces = []
        self.__piece_index = 0

    def add_piece(self, piece):
        """Adds a chess piece into the board.

        Arguments:
            piece {PieceModel} -- New piece to be added
        """
        self.__piece_index += 1
        piece.id = f"{piece.id}{self.__piece_index}"
        self.board_pieces.append(piece)

    def get_piece_by_id(self, piece_id):
        """Returns the piece with the given id.

        Arguments:
            piece_id {str} -- Id to locate the desired piece

        Raises:
            PieceNotFoundError: When it's not possible to find the piece

        Returns:
            PieceModel -- The piece with the specified id
        """
        for piece in self.board_pieces:
            if piece.id == piece_id:
                return piece

        raise PieceNotFoundError("None piece found with the specified id")
