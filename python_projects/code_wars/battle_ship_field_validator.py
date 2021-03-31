battleField = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def possible(y, x, field):
    if x == 0:
        if field[y - 1][x + 1] == 1 or field[y + 1][x + 1] == 1:
            return False
    if x == 10:
        if field[y - 1][x - 1] == 1 or field[y + 1][x - 1] == 1:
            return False
    if y == 0:
        if field[y + 1][x - 1] == 1 or field[y + 1][x + 1] == 1:
            return False
    if y == 10:
        if field[y - 1][x - 1] == 1 or field[y - 1][x + 1] == 1:
            return False
    else:
        if field[y - 1][x - 1] == 1 or field[y + 1][x - 1] == 1 or field[y - 1][x + 1] == 1 or field[y + 1][x + 1] == 1:
            return False
    return True


def validate_battlefield(field):
    a = 0
    for i in field:
        a += sum(i)
    print(a)
    if a == 20:
        for y in range(10):
            for x in range(10):
                if field[y][x] == 1:
                    if not possible(y, x, field):
                        return False
    else:
        return False
    return True


print(validate_battlefield(battleField))
