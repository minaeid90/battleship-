import unittest
from battleship.api import app


class TestCreateBattleShip(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_correct_representation_of_ships(self):
        
        data = {
            "ships": [
                {
                    "x": 2,
                    "y": 1,
                    "size": 4,
                    "direction": "H"
                },
                {
                    "x": 7,
                    "y": 4,
                    "size": 3,
                    "direction": "V"
                },
                {
                    "x": 3,
                    "y": 5,
                    "size": 2,
                    "direction": "V"
                },
                {
                    "x": 6,
                    "y": 8,
                    "size": 1,
                    "direction": "H"
                }
            ]
        }
        response = self.app.post('/battleship', data=data)
        assert response.status_code == 200

    def test_overlap_representation_of_ships(self):
        data = {
            "ships": [
                {
                    "x": 5,
                    "y": 5,
                    "size": 4,
                    "direction": "H"
                },
                {
                    "x": 7,
                    "y": 4,
                    "size": 3,
                    "direction": "V"
                },
                {
                    "x": 3,
                    "y": 5,
                    "size": 2,
                    "direction": "V"
                },
                {
                    "x": 6,
                    "y": 8,
                    "size": 1,
                    "direction": "H"
                }
            ]
        }
        response = self.app.post('/battleship', data=data)
        assert response.status_code == 400


if __name__ == "__main__":
    unittest.main()
