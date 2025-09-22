from byu_pytest_utils import max_score, dialog, test_files


@max_score(0.5)
@dialog(test_files / "doubles.dialog.txt","doubles.py")
def test_doubles(): ...


@max_score(0.5)
@dialog(test_files / "doubles2.dialog.txt","doubles.py")
def test_doubles_again(): ...

