from byu_pytest_utils import max_score, test_files, dialog


@max_score(25)
@dialog(
    test_files / "expenses.dialog.txt",
    "expenses.py"
)
def test_expenses_1(): ...


@max_score(25)
@dialog(
    test_files / "expenses2.dialog.txt",
    "expenses.py"
)
def test_expenses_2(): ...
