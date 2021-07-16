def count_letters_and_punctuations(text):
    result = []
    for line in text:
        line = line[:-1]
        punctuations = 0
        letters = 0
        for word in line:
            for char in word:
                if char in ["-", ",", ".", "!", "?", "'"]:
                    punctuations += 1
                elif char.isalpha():
                    letters += 1
        result.append(f'{line} ({letters})({punctuations})')
    return result


def line_number(text):
    result = []
    for i in range(1, len(text) + 1):
        result.append(f"Line {i}: {text[i - 1]}")
    return result


def write_lines(l):
    with open("output.txt", "w") as output_data_file:
        output_data_file.writelines("\n".join(l))


with open("text.txt") as input_data_file:
    count_symbols = count_letters_and_punctuations(input_data_file.readlines())
    numbered_lines = line_number(count_symbols)
    write_lines(numbered_lines)
