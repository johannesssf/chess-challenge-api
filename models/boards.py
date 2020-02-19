"""Chess board
"""

class NotEmptySquareError(Exception):
    pass


class NotAvailableSquaresInBoardError(Exception):
    pass


class NotValidSquareLocationError(Exception):
    pass


class BoardModel:

    def __init__(self):
        """Creates a 64-square board.
        """
        self.squares = {f'{r}{c}': None for r in range(1, 9) for c in 'ABCDEFGH'}
        self.__pieces_index = 0

    def set_piece(self, location, piece):
        """Adds a chess piece in a board square location.

        Arguments:
            location {str} -- Board square location indexed by 1A 1B ... 8G 8H
            piece {Piece} -- Piece to add in the board

        Raises:
            NotEmptySquareError: In an attempt to use an occupied square
        """
        if self.get_piece_by_location(location) is not None:
            raise NotEmptySquareError("Board square already in use")

        self.__pieces_index += 1
        piece.id = f"{piece.id}{self.__pieces_index}"
        self.squares[location] = piece

    def get_piece_by_location(self, location):
        """Returns a piece in a specific board square location.

        Arguments:
            location {str} -- Board square location indexed by 1A 1B ... 8G 8H

        Raises:
            NotValidSquareLocationError: In an attempt to access an invalid
            key location

        Returns:
            Piece -- The piece in specified location or None if it's empty
        """
        if location not in self.squares:
            raise NotValidSquareLocationError("Boad square not found")

        return self.squares[location]
