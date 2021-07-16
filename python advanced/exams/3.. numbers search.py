def numbers_searching(*args):
    missing_number = 0
    duplicate_numbers = []
    args = sorted(args)
    for num in args:
        count = args.count(num)
        if count != 1:
            duplicate_numbers.append(num)
    for i in range(min(args), max(args)):
        if i not in args:
            missing_number = i
    return [missing_number, sorted(list(set(duplicate_numbers)))]


print(numbers_searching(1, 2, 3, 4, 4, 3, 5, 5, 7))
