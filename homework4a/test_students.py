from byu_pytest_utils import dialog, test_files, max_score


@max_score(5)
@dialog(test_files / "students.dialog.txt", "students.py")
def test_students(): ...


@max_score(5)
@dialog(test_files / "students2.dialog.txt", "students.py")
def test_students2(): ...
