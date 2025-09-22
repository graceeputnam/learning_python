from byu_pytest_utils import max_score, dialog, test_files



@max_score(1)
@dialog(test_files / "upper_vowels.dialog.txt", "upper_vowels.py")
def test_upper_vowels(): ...


@max_score(1)
@dialog(test_files / "upper_vowels2.dialog.txt", "upper_vowels.py")
def test_upper_vowels_again(): ...
