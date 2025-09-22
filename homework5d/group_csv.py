from string import punctuation
import sys


def group_em(lines, keys, items):
    new = {}
    key = int(keys)
    item = int(items)
    for line in lines:
        new_line = line.split(",")
        if new_line[key] not in new:
            new[new_line[key]] = []
        if new_line[key] in new:
            new[new_line[key]].append(new_line[item])
    return new


def read_file(file):
    with open(file) as file:
        return file.readlines()


def print_dict(dict):
    for key in dict.keys():
        print(f"{key}: {dict[key]}")


def main(input, keys, items):
    lines = read_file(input)
    grouped = group_em(lines, keys, items)
    print_dict(grouped)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
# :)
