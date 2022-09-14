import os

class SquareBoard:

    def __init__(self, N):
        self.N = N
        self.board = [["-" for _ in range(N)] for _ in range(N)]

    def print_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def set_queen_at(self, i, j):
        self.board[i][j] = "**"


    def is_queen(self, i, j):
        return self.board[i][j] == "**"
    

    def get_queen_on(self, i):
        for j in range(self.N):
            if self.is_queen(i, j):
                return j
        raise ValueError("programmer error: no queen on row")


    def unset_queen_on(self, i):
        self.board[i] = ["-" for _ in range(self.N)]


    def num_queens(self):
        num_queens = 0
        for i in range(self.N):
            for j in range(self.N):
                if self.is_queen(i, j):
                    num_queens += 1
        return num_queens

    def is_valid_row(self, i, j):
        for k in range(self.N):
            if self.is_queen(i, k) and k != j:
                return False
        return True

    def is_valid_col(self, i, j):
        for k in range(self.N):
            if self.is_queen(k, j) and k != i:
                return False
        return True
    
    def is_valid_diag(self, i, j):
        for k in range(1, self.N):
            if i + k < self.N:
                if j + k < self.N:
                    if self.is_queen(i + k, j + k):
                        return False
                if j - k >= 0:
                    if self.is_queen(i + k, j - k):
                        return False
            if i - k >= 0:
                if j + k < self.N:
                    if self.is_queen(i - k, j + k):
                        return False
                if j - k >= 0:
                    if self.is_queen(i - k, j - k):
                        return False
        return True


    def is_valid_move(self, i, j):
        if j >= self.N:
            # this is to catch the case where the Q is
            # at the last possible column in a row
            # and we are backtracking to the previous row
            return False
        if self.num_queens() > 8:
            return False
        if not self.is_valid_row(i, j):
            return False
        if not self.is_valid_col(i, j):
            return False
        if not self.is_valid_diag(i, j):
            return False
        return True


    def print_solutions(self):
        row = 0
        col = 0
        nsols = 1

        while row >= 0:

            if row < self.N:
            # we are searching for a solution

                if self.is_valid_move(row, col):
                    self.set_queen_at(row, col)
                    row += 1
                    col = 0
                
                else:
                    if col < self.N - 1:
                        col += 1
                    else:
                        # backtrack
                        if row == 0:
                            # no solutions
                            return

                        row -= 1
                        col = self.get_queen_on(row) + 1
                        self.unset_queen_on(row)

            else:
                # we have found a solution
                print("Solution " + str(nsols))
                self.print_board()
                nsols += 1
                input("Enter for next solution: ")
                os.system("clear")

                row -= 1
                col = self.get_queen_on(row) + 1
                self.unset_queen_on(row)
       

b = SquareBoard(8)
b.print_board()
print()
b.print_solutions()
