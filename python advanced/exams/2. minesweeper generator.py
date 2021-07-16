def matrix_creator(n):
    return [[0 for _ in range(n)] for _ in range(n)]


def mine_placement(matrix, bomb_r, bomb_c):
    matrix[bomb_r][bomb_c] = "*"
    return matrix


def is_valid(matrix, r, c):
    if 0 <= r < matrix_size and 0 <= c < matrix_size and matrix[r][c] != "*":
        return True


def calc_cell_numbers(matrix, bomb_r, bomb_c):
    # diagonal top left
    if is_valid(matrix, bomb_r - 1, bomb_c - 1):
        matrix[bomb_r - 1][bomb_c - 1] += 1
    # upper
    if is_valid(matrix, bomb_r - 1, bomb_c):
        matrix[bomb_r - 1][bomb_c] += 1
    # diagonal top right
    if is_valid(matrix, bomb_r - 1, bomb_c + 1):
        matrix[bomb_r - 1][bomb_c + 1] += 1
    # left
    if is_valid(matrix, bomb_r, bomb_c - 1):
        matrix[bomb_r][bomb_c - 1] += 1
    # right
    if is_valid(matrix, bomb_r, bomb_c + 1):
        matrix[bomb_r][bomb_c + 1] += 1
    # diagonal bot left
    if is_valid(matrix, bomb_r + 1, bomb_c - 1):
        matrix[bomb_r + 1][bomb_c - 1] += 1
    # bot
    if is_valid(matrix, bomb_r + 1, bomb_c):
        matrix[bomb_r + 1][bomb_c] += 1
    # diagonal bot right\
    if is_valid(matrix, bomb_r + 1, bomb_c + 1):
        matrix[bomb_r + 1][bomb_c + 1] += 1
    return matrix


matrix_size = int(input())
mines_count = int(input())
matrix = matrix_creator(matrix_size)

for _ in range(mines_count):
    mine_row, mine_col = map(int, input().strip("()").split(", "))
    mine_placement(matrix, mine_row, mine_col)
    calc_cell_numbers(matrix, mine_row, mine_col)


for r in matrix:
    print(*r)
