class Ship():

    def __init__(self, x, y, size, direction):

        self.x = x-1
        self.y = y-1
        self.size = size
        self.direction = direction
        self.num_hits = 0

    def hit(self):
        self.num_hits += 1
        if self.num_hits == self.size:
            return 'SINK'
        return 'HIT'

    @property
    def pieces(self):
        location = []
        if self.direction == 'H':
            for i in range(self.size):
                location.append((self.x+i, self.y))
        elif self.direction == 'V':
            for i in range(self.size):
                location.append((self.x, self.y+i))

        return location


class Board():
    BOARD_SIZE = 10

    def __init__(self, board, ships=[]):
        self.board = board
        self.ships = ships

    def set_ships(self, data):
        created, overlap, out_bound = False, False, False
        for item in data:
            ship = Ship(item['x'], item['y'], item['size'], item['direction'])
            for i in range(ship.size):
                if ship.direction == 'H':
                    if ship.x+ship.size >= Board.BOARD_SIZE:
                        out_bound = True
                    if self.board[ship.x+i][ship.y] != 'X':
                        self.board[ship.x+i][ship.y] = 'X'
                        self.ships.append(ship)
                    if self.board[ship.x+i][ship.y] == 'X':
                        overlap = True
                elif ship.direction == 'V':
                    if ship.y+ship.size >= Board.BOARD_SIZE:
                        out_bound = True
                    if self.board[ship.x][ship.y+i] != 'X':
                        self.board[ship.x][ship.y+i] = 'X'
                        self.ships.append(ship)
                    if self.board[ship.x][ship.y+i] == 'X':
                        overlap = True
        return created, overlap, out_bound

    def battle(self, shot):
        shot = (shot['x']-1, shot['y']-1)
        if shot[0] >= self.BOARD_SIZE or shot[1] >= self.BOARD_SIZE:
            return 0
        for ship in self.ships:
            if shot in ship.pieces:
                state = ship.hit()
                return state
