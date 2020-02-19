import pytest

from models.pieces import (
    PieceModel,
    InvalidPieceColorError,
    InvalidPieceNameError,
)
from models.boards import (
    BoardModel,
    NotEmptySquareError,
    NotAvailableSquaresInBoardError,
    NotValidSquareLocationError,
)


def test_piece_creation_exeptions():
    with pytest.raises(InvalidPieceNameError):
        PieceModel('Horse', 'BLACK')

    with pytest.raises(InvalidPieceNameError):
        PieceModel('God', 'White')

    with pytest.raises(InvalidPieceColorError):
        PieceModel('King', 'BlUE')

    with pytest.raises(InvalidPieceColorError):
        PieceModel('Bishop', 'Red')


def test_piece_creation():
    king = PieceModel('king', 'black')
    assert f"{king.name[:2]}{king.color[0]}" in king.id
    queen = PieceModel('queen', 'white')
    assert f"{queen.name[:2]}{queen.color[0]}" in queen.id


def test_board_set_piece():
    black_king = PieceModel('King', 'Black')
    white_king = PieceModel('King', 'White')
    black_rook = PieceModel('Rook', 'Black')
    white_bishop = PieceModel('Bishop', 'White')
    board = BoardModel()
    board.set_piece('1A', black_king)
    board.set_piece('1B', white_king)
    board.set_piece('3H', black_rook)
    board.set_piece('8G', white_bishop)


def test_board_set_piece_exceptions():
    black_queen = PieceModel('Queen', 'Black')
    white_pawn = PieceModel('Pawn', 'White')
    black_knight = PieceModel('Knight', 'Black')
    white_bishop = PieceModel('Bishop', 'White')
    board = BoardModel()

    board.set_piece('5C', black_queen)
    with pytest.raises(NotEmptySquareError):
        board.set_piece('5C', white_pawn)

    board.set_piece('7A', black_knight)
    with pytest.raises(NotEmptySquareError):
        board.set_piece('7A', white_bishop)


def test_board_get_piece_by_location():
    black_king = PieceModel('King', 'Black')
    white_bishop = PieceModel('Bishop', 'White')
    board = BoardModel()
    board.set_piece('1A', black_king)
    board.set_piece('8G', white_bishop)
    assert board.get_piece_by_location('1A') is not None
    assert board.get_piece_by_location('8G') is not None
    assert board.get_piece_by_location('3E') is None
    assert board.get_piece_by_location('3A') is None


def test_board_get_piece_by_location_exceptions():
    board = BoardModel()

    with pytest.raises(NotValidSquareLocationError):
        board.get_piece_by_location('9H')

    with pytest.raises(NotValidSquareLocationError):
        board.get_piece_by_location('7Z')

    with pytest.raises(NotValidSquareLocationError):
        board.get_piece_by_location(66)

    with pytest.raises(NotValidSquareLocationError):
        board.get_piece_by_location('AAA')

    with pytest.raises(NotValidSquareLocationError):
        board.get_piece_by_location(None)
