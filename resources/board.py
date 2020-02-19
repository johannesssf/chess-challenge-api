from flask import jsonify
from flask_restful import Resource, reqparse
from models.board import BoardModel, PieceNotFoundError
from models.piece import (
    PieceModel,
    InvalidPieceNameError,
    InvalidPieceColorError,
    calculate_knight_moves,
)


board = BoardModel()


class Board(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!",
                        )
    parser.add_argument('color',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!",
                        )

    def post(self):
        data = Board.parser.parse_args()
        name = data['name']
        color = data['color']
        try:
            new_piece = PieceModel(name, color)
        except InvalidPieceNameError:
            return {"msg": "Invalid chess piece name: {}".format(name)}, 400
        except InvalidPieceColorError:
            return {"msg": "Invalid chess piece color: {}".format(color)}, 400

        new_piece = PieceModel(name, color)
        board.add_piece(new_piece)

        return {"piece_id": new_piece.id}, 200


class BoardPieces(Resource):

    def get(self):
        pieces = []
        for piece in board.board_pieces:
            pieces.append({
                'id': piece.id,
                'name': piece.name,
                'color': piece.color
            })

        return {"board_pieces": pieces}, 200


class BoardPieceCoord(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('coord',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!",
                        )
    parser.add_argument('piece_id',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!",
                        )

    def get(self):
        data = BoardPieceCoord.parser.parse_args()
        coord = data['coord']
        piece_id = data['piece_id']

        try:
            piece = board.get_piece_by_id(piece_id)
        except PieceNotFoundError:
            return {"msg": f"There is no piece with id: {piece_id}"}, 404

        moves = {}
        if piece.name == "Knight":
            first_turn_moves = calculate_knight_moves(coord)
            second_turn_moves = {}
            for move in first_turn_moves:
                second_turn_moves[move] = calculate_knight_moves(move)
            moves['first_turn'] = first_turn_moves
            moves['second_turn'] = second_turn_moves

        return {
            "piece_id": piece_id,
            "coord": coord,
            "possible_moves": moves,
        }

