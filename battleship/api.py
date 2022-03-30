
import json
from http import HTTPStatus
from xml.dom import ValidationErr

from flask import Flask, jsonify, request
from .game import Board
app = Flask(__name__)


@app.route('/battleship', methods=['POST'])
def create_battleship_game():

    game_board = [[' '] * 10 for i in range(10)]
    global board
    board = Board(game_board)
    payload = json.loads(request.data)
    created = board.set_ships(data=payload)
    board.print_board()
    if not created:
        return jsonify({}), HTTPStatus.BAD_REQUEST
    return jsonify({}), HTTPStatus.OK


@app.route('/battleship', methods=['PUT'])
def shot():
    return jsonify({}), HTTPStatus.OK


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():

    return jsonify({}), HTTPStatus.OK
