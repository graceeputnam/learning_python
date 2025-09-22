def get_grades():
    print("Enter scores for each student.")
    print("Enter a blank student name to end.")
    responses = []
    while True:
        name = input("Student: ")
        if name == "":
            break
        score = int(input("Score: "))
        student = (name, score)
        responses.append(student)
    return responses


def bonus_time(grades, bonus):
    new_grades = []
    for i in grades:
        name, grade = i
        score = round((grade * (1 + float(bonus))), 1)
        new_score = name, score
        new_grades.append(new_score)
    return new_grades


def above_cutoff(grades, cutoff):
    print("High Scores:")
    new_list = []
    for i in grades:
        name, score = i
        if score > int(cutoff):
            new_list.append(i)
    for i in new_list:
        print(f"- {i[1]}: {i[0]}")


def main():
    grades = get_grades()
    bonus = input("Bonus: ")
    cutoff = input("Cutoff: ")
    bumped_grades = bonus_time(grades, bonus)
    above_cutoff(bumped_grades, cutoff)


if __name__ == '__main__':
    main()


