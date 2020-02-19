"""Chess piece
"""

class InvalidPieceNameError(Exception):
    pass


class InvalidPieceColorError(Exception):
    pass


PIECES_COLOR = ('White', 'Black')
PIECES_NAME = ('King', 'Queen', 'Rook', 'Bishop', 'Knight', 'Pawn')


class PieceModel:

    def __init__(self, name, color):
        """Creates a new chess piece specified name and color.

        Arguments:
            name {str} -- Chess piece name: King|Queen|Rook|Bishop|Knight|Pawn
            color {srt} -- Chess piece color: Black|White

        Raises:
            InvalidPieceNameError: When an invalid piece name is used
            InvalidPieceColorError: When an invalid piece color is used
        """
        if name.capitalize() not in PIECES_NAME:
            raise InvalidPieceNameError(f"Name must be in ({PIECES_NAME})")

        if color.capitalize() not in PIECES_COLOR:
            raise InvalidPieceColorError(f"Color must be ({PIECES_COLOR})")

        self.name = name.capitalize()
        self.color = color.capitalize()
        self.id = f"{self.name[:2]}{self.color[0]}"
