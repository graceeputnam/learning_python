from byu_pytest_utils import max_score, test_files, dialog


@max_score(3.5)
@dialog(
    test_files/"true-blue.dialog.txt",
    "blue_score.py"
)
def test_blue_score(): ...


@max_score(3.5)
@dialog(
    test_files/"true-blue2.dialog.txt",
    "blue_score.py"
)
def test_blue_score2(): ...
