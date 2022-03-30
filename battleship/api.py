import json
from http import HTTPStatus
from typing import overload

from flask import Flask,  jsonify, request

from .game import Board

app = Flask(__name__)


@app.route('/battleship', methods=['POST'])
def create_battleship_game():
    init_board = [[' ']*10 for i in range(10)]
    global board
    board = Board(init_board)
    payload = json.loads(request.data)
    created, overlap, outbound = board.set_ships(data=payload['ships'])
    board.print_board()
    if outbound:
        return jsonify({"error": "outbound"}, HTTPStatus.BAD_REQUEST)
    if overlap:
        print('overlap')
        return jsonify({"error": "overlap"}, HTTPStatus.BAD_REQUEST)

    if not created:
        return jsonify({"error": "not created"}, HTTPStatus.BAD_REQUEST)

    return jsonify({"detail": "Ships are located on board game"}), HTTPStatus.OK


@app.route('/battleship', methods=['PUT'])
def shot():
    try:
        payload = json.loads(request.data)
        result = board.battle(payload)
        if result == 0:
            return jsonify({}), HTTPStatus.BAD_REQUEST
        return jsonify({"result": result}), HTTPStatus.OK
    except NameError:
        return jsonify({"error": "there is no game at this moment"}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        return jsonify({"error": e}), HTTPStatus.BAD_REQUEST


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():
    global board
    del board
    return jsonify({}), HTTPStatus.OK
