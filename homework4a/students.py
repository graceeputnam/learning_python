
def get_list():
    responses = []
    while True:
        print("Enter a student.")
        name = input("Name: ")
        if name == "":
            break
        hometown = input("Hometown: ")
        school = input("School: ")
        studentlist = (name, hometown, school)
        responses.append(studentlist)
    return responses


def BYU_students(students):
    BYU = []
    other = []
    for name, hometown, school in students:
        if school == "BYU":
            BYU.append(name)
        else:
            other.append(name)
    students = BYU, other
    return students


def print_byu(students):
    print("BYU Students:")
    BYU, other = students
    for name in BYU:
        name = name.upper()
        print(f"- {name}")
    print("Other Students:")
    for name in other:
        print(f"- {name}")


def main():
    students = get_list()
    print_byu(BYU_students(students))



if __name__ == "__main__":
    main()
