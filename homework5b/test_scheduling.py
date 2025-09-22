from byu_pytest_utils import max_score, dialog, test_files


@max_score(5)
@dialog(
    test_files/"student_schedule.dialog.txt",
    "scheduling.py",
    test_files/"students.txt",
    test_files/"timeslots.txt"
)
def test_scheduling_students(): ...


@max_score(5)
@dialog(
    test_files/"teacher_schedule.dialog.txt",
    "scheduling.py",
    test_files/"teachers.txt",
    test_files/"timeslots.txt"
)
def test_scheduling_teachers(): ...