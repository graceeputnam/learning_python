from byu_pytest_utils import max_score, dialog, test_files


@max_score(1)
@dialog(test_files / "remove_punctuation.dialog.txt","remove_punctuation.py")
def test_remove_punctuation(): ...


@max_score(1)
@dialog(test_files / "remove_punctuation2.dialog.txt","remove_punctuation.py")
def test_remove_punctuation_2(): ...

