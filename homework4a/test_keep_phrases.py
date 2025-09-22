from byu_pytest_utils import max_score, dialog, test_files


@max_score(1)
@dialog(test_files / "keep_big_phrases.dialog.txt","keep_big_phrases.py")
def test_keep_big_phrases(): ...


@max_score(1)
@dialog(test_files / "keep_big_phrases2.dialog.txt","keep_big_phrases.py")
def test_keep_big_phrases2(): ...
