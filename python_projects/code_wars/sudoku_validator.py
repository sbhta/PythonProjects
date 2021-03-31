class Sudoku(object):
    def __init__(self, data):
        self.data = data
        # what is the N
        self.N = len(self.data)

    def is_valid(self):
        N = self.N
        newArray = []
        for y in range(N):
            newArray.append(self.data[y][0])
            for x in range(N):
                try:
                    if self.data[y][x] > N or self.data[y][x] <= 0 or type(self.data[y][x]) != int:
                        return False
                except Exception:
                    return False
        if len(newArray) != N:
            return False
        if N % 1 != 0:
            return False
        return True


goodSudoku = Sudoku([
    [7, 8, 4, 1, 5, 9, 3, 2, 6],
    [5, 3, 9, 6, 7, 2, 8, 4, 1],
    [6, 1, 2, 4, 3, 8, 7, 5, 9],

    [9, 2, 8, 7, 1, 5, 4, 6, 3],
    [3, 5, 7, 8, 4, 6, 1, 9, 2],
    [4, 6, 1, 9, 2, 3, 5, 8, 7],

    [8, 7, 6, 3, 9, 4, 2, 1, 5],
    [2, 4, 3, 5, 6, 1, 9, 7, 8],
    [1, 9, 5, 2, 8, 7, 6, 3, 4],
])

print(goodSudoku.is_valid())
