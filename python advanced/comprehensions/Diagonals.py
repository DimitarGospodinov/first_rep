def make_matrix():
    matrix = [list(map(int, input().split(", "))) for _ in range(rows)]
    return matrix


def first_diagonal(m, rows):
    row_one = [m[i][i] for i in range(rows)]
    return f"First diagonal: {', '.join(map(str, row_one))}. Sum: {sum(row_one)}"


def second_diagonal(m, rows):
    row_two = [m[i][rows - i - 1] for i in range(rows)]
    return f"Second diagonal: {', '.join(map(str, row_two))}. Sum: {sum(row_two)}"


rows = int(input())
matrix = make_matrix()
print(first_diagonal(matrix, rows))
print(second_diagonal(matrix, rows))
