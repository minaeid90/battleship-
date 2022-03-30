class Board():
    BOARD_SIZE = 10

    def __init__(self, board, ships=[]):
        self.board = board
        self.ships = ships

    def print_board(self):

        print("  1 2 3 4 5 6 4 8 9 10")
        print("  +-+-+-+-+-+-+-+-+-+-")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1

    def validate_ship(self, sh):
        if self.ships:
            for ship in self.ships:
                for point in ship.points:
                    if point in sh.points:
                        return False
        return True

    def add_ship(self, sh):
        if sh not in self.ships:
            self.ships.append(sh)

    def set_ships(self, data):
        for item in data['ships']:
            ship = Ship(item['x'], item['y'], item['size'], item['direction'])
            is_valid = self.validate_ship(ship)
            if is_valid:
                self.add_ship(ship)
                return True
            else:
                return False


class Ship():

    def __init__(self, x, y, size, direction):
        self.x = x-1
        self.y = y-1
        self.size = size
        self.direction = direction
        self.num_hits = 0

    @property
    def points(self):
        coordinates = []
        if self.direction == 'H':
            for i in range(self.size):
                coordinates.append((self.x+i, self.y))
        elif self.direction == 'V':
            for i in range(self.size):
                coordinates.append((self.x, self.y+i))
        return coordinates
