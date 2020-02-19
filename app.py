from flask import Flask
from flask_restful import Api
from resources.board import Board, BoardPieces, BoardPieceCoord


app = Flask(__name__)
api = Api(app)

api.add_resource(Board, '/addpiece')
api.add_resource(BoardPieces, '/pieces')
api.add_resource(BoardPieceCoord, '/piece')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
