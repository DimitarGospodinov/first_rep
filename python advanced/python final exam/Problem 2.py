def make_matrix():
    return [input().split() for _ in range(5)]


def find_starting_loc(m):
    for row in range(len(m)):
        for col in range(len(m)):
            if m[row][col] == "A":
                return row, col


def find_targets(m):
    targets_count = 0
    for row in range(len(m)):
        for col in range(len(m)):
            if m[row][col] == "x":
                targets_count += 1
    return targets_count


def is_index_in(row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True


def is_valid_move(row, col):
    if is_index_in(row, col):
        if matrix[row][col] == "*":
            return True


def is_target(row, col):
    if is_index_in(row, col):
        if matrix[row][col] == "x":
            return True


matrix = make_matrix()
current_loc = find_starting_loc(matrix)
n_moves = int(input())
targets_shot = 0
targets_count = find_targets(matrix)
is_completed = False
targets_shot_list = []
for _ in range(n_moves):
    command = input().split()
    if command[0] == "move":
        spaces = int(command[2])
        if command[1] == "left":
            if is_valid_move(current_loc[0], current_loc[1] - spaces):
                current_loc = current_loc[0], current_loc[1] - spaces
        elif command[1] == "right":
            if is_valid_move(current_loc[0], current_loc[1] + spaces):
                current_loc = current_loc[0], current_loc[1] + spaces
        elif command[1] == "down":
            if is_valid_move(current_loc[0] + spaces, current_loc[1]):
                current_loc = current_loc[0] + spaces, current_loc[1]
        elif command[1] == "up":
            if is_valid_move(current_loc[0] - spaces, current_loc[1]):
                current_loc = current_loc[0] - spaces, current_loc[1]

    if command[0] == "shoot":
        if command[1] == "left":
            for i in range(len(matrix)):
                if is_target(current_loc[0], current_loc[1] - i):
                    targets_shot += 1
                    matrix[current_loc[0] - i][current_loc[1]] = "."
                    targets_shot_list.append([current_loc[0], current_loc[1] - i])
                    break
        elif command[1] == "right":
            for i in range(len(matrix)):
                if is_target(current_loc[0], current_loc[1] + i):
                    targets_shot += 1
                    matrix[current_loc[0]][current_loc[1] + i] = "."
                    targets_shot_list.append([current_loc[0], current_loc[1] + i])
                    break
        elif command[1] == "down":
            for i in range(len(matrix)):
                if is_target(current_loc[0] + i, current_loc[1]):
                    targets_shot += 1
                    matrix[current_loc[0] + i][current_loc[1]] = "."
                    targets_shot_list.append([current_loc[0] + i, current_loc[1]])
                    break
        elif command[1] == "up":
            for i in range(len(matrix)):
                if is_target(current_loc[0] - i, current_loc[1]):
                    targets_shot += 1
                    matrix[current_loc[0] - i][current_loc[1]] = "."
                    targets_shot_list.append([current_loc[0] - i, current_loc[1]])
                    break
    if targets_count == targets_shot:
        is_completed = True
        break
if is_completed:
    print(f"Training completed! All {targets_count} targets hit.")
    for x in targets_shot_list:
        print(x)
else:
    print(f"Training not completed! {targets_count - targets_shot} targets left.")
    for x in targets_shot_list:
        print(x)
