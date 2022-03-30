
from http import HTTPStatus

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/battleship', methods=['POST'])
def create_battleship_game():

    return jsonify({}), HTTPStatus.OK


@app.route('/battleship', methods=['PUT'])
def shot():
    return jsonify({}), HTTPStatus.OK


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():

    return jsonify({}), HTTPStatus.OK
