from byu_pytest_utils import max_score, dialog, test_files


@max_score(1)
@dialog(test_files / "replace_digits.dialog.txt","replace_digits.py",)
def test_replace_digits_with_asterisk(): ...


@max_score(1)
@dialog(test_files / "replace_digits2.dialog.txt","replace_digits.py")
def test_replace_digits_with_asterisk2(): ...


