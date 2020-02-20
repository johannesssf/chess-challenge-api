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


def calculate_knight_moves(board_location):
    """Calculates all possible moves of a Knight.

    Arguments:
        board_location {str} -- Valid location of a 64-square board

    Returns:
        [list] -- All valid moves from the initial location
    """
    convert_to_num = {char: idx for idx, char in enumerate('ABCDEFGH', 1)}
    convert_to_char = {idx: char for idx, char in enumerate('ABCDEFGH', 1)}
    line = int(board_location[0])
    col = convert_to_num[board_location[1].upper()]

    # calculate all possible moves of our Knight
    possible_moves = []
    possible_moves.append((line - 2, col + 1))
    possible_moves.append((line - 2, col - 1))
    possible_moves.append((line + 2, col + 1))
    possible_moves.append((line + 2, col - 1))
    possible_moves.append((line + 1, col + 2))
    possible_moves.append((line - 1, col + 2))
    possible_moves.append((line + 1, col - 2))
    possible_moves.append((line - 1, col - 2))

    # validate if generated moves are inside of a 64-square board
    valid_moves = []
    for line, col in possible_moves:
        if 0 < line < 9 and 0 < col < 9:
            valid_moves.append(f"{line}{convert_to_char[col]}")

    return valid_moves
