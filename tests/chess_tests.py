import pytest

from models.piece import (
    PieceModel,
    InvalidPieceColorError,
    InvalidPieceNameError,
    calculate_knight_moves,
)
from models.board import (
    BoardModel,
    PieceNotFoundError,
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


def test_board_add_piece():
    black_king = PieceModel('King', 'Black')
    white_king = PieceModel('King', 'White')
    black_rook = PieceModel('Rook', 'Black')
    white_bishop = PieceModel('Bishop', 'White')
    board = BoardModel()
    board.add_piece(black_king)
    assert black_king.id == "KiB1"
    board.add_piece(white_king)
    assert white_king.id == "KiW2"
    board.add_piece(black_rook)
    assert black_rook.id == "RoB3"
    board.add_piece(white_bishop)
    assert white_bishop.id == "BiW4"


def test_board_get_piece_by_id():
    black_king = PieceModel('King', 'Black')
    white_bishop = PieceModel('Bishop', 'White')
    board = BoardModel()
    board.add_piece(black_king)
    board.add_piece(white_bishop)
    assert board.get_piece_by_id('KiB1') is black_king
    assert board.get_piece_by_id('BiW2') is white_bishop


def test_board_get_piece_by_id_exceptions():
    board = BoardModel()

    with pytest.raises(PieceNotFoundError):
        board.get_piece_by_id('KiB1')

    with pytest.raises(PieceNotFoundError):
        board.get_piece_by_id('BiW2')


def test_knight_move_calculator():
    assert calculate_knight_moves('1A') == ['3B', '2C']
    assert calculate_knight_moves('8H') == ['6G', '7F']
    assert calculate_knight_moves('2e') == ['4F', '4D', '3G', '1G', '3C', '1C']
    assert calculate_knight_moves('5b') == ['3C', '3A', '7C', '7A', '6D', '4D']
    assert calculate_knight_moves('4E') == ['2F', '2D', '6F', '6D', '5G', '3G', '5C', '3C']
