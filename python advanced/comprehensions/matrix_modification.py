def make_matrix(r):
    m = [[int(x) for x in input().split()] for _ in range(r)]
    return m


def if_valid_index(r, c):
    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        return True
    else:
        print("Invalid coordinates")


def add(m, r, c, v):
    if if_valid_index(r, c):
        m[r][c] += v
        return m


def subtract(m, r, c, v):
    if if_valid_index(r, c):
        m[r][c] -= v
        return m


matrix_size = int(input())
matrix = make_matrix(matrix_size)

while True:
    command = input()
    if command == "END":
        break
    action, row, col, value = command.split()
    row = int(row)
    col = int(col)
    value = int(value)
    if action == "Add":
        add(matrix, row, col, value)
    elif action == "Subtract":
        subtract(matrix, row, col, value)

for i in matrix:
    print(" ".join(map(str, i)))
