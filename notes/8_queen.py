class SquareBoard:

    def __init__(self, N):
        self.N = N
        self.board = [["-" for _ in range(N)] for _ in range(N)]

    def print_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

b = SquareBoard(8)
b.print_board()
