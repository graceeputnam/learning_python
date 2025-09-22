import sys


def read_file(input):
    list1 = []
    with open(input) as file:
        return file.readlines()


def create_dict(lines, time):
    new = {}
    for line, time in zip(lines, time):
        new[line.strip()] = time.strip()
    return new


def find_names(dict):
    while True:
        name = input("Name: ")
        if name == '':
            break
        elif name in dict:
            print(f"{name} is assigned {dict[name]}")
        else:
            print(f"{name} is not assigned a timeslot")


def main(input, times):
    lines = read_file(input)
    time = read_file(times)
    dict = create_dict(lines, time)
    find_names(dict)


if __name__ == '__main__':
   main(sys.argv[1], sys.argv[2])
# :)
