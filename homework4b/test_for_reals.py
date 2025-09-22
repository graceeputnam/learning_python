from byu_pytest_utils import max_score, dialog, test_files


@max_score(0.5)
@dialog(test_files / "for_reals.dialog.txt","for_reals.py")
def test_for_reals(): ...


@max_score(0.5)
@dialog(test_files / "for_reals2.dialog.txt","for_reals.py")
def test_for_reals_again(): ...

