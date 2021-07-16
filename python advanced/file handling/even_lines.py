import re


def only_even_lines(f):
    return [f[x][:-1] for x in range(len(f)) if x % 2 == 0]


def replace_symbols(text):
    for letter in text:
        words_list = " ".join(reversed(letter.split()))
        text = re.sub(r"[-,\.\!\?]", "@", words_list)
        print("".join(text))

with open("text.txt") as file:
    text = only_even_lines(file.readlines())
    replace_symbols(text)
