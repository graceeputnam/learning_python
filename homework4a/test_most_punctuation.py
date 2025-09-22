from byu_pytest_utils import max_score, dialog, test_files


@max_score(.66)
@dialog(test_files / "most_punctuation.dialog.txt","most_punctuation.py")
def test_most_punctuation(): ...


@max_score(.67)
@dialog(test_files / "most_punctuation2.dialog.txt","most_punctuation.py")
def test_most_punctuation2(): ...


@max_score(.67)
@dialog(test_files / "most_punctuation3.dialog.txt","most_punctuation.py")
def test_most_punctuation3(): ...


