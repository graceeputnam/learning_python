from byu_pytest_utils import max_score, dialog, test_files


@max_score(1)
@dialog(test_files / "whitespace.dialog.txt","count_whitespace.py")
def test_count_whitespace(): ...


@max_score(1)
@dialog(test_files / "whitespace2.dialog.txt","count_whitespace.py")
def test_count_whitespace2(): ...
