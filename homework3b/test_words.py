from byu_pytest_utils import max_score, test_files, dialog


@max_score(5)
@dialog(
    test_files / "words_python.dialog.txt",
    "words.py"
)
def test_words(): ...


@max_score(5)
@dialog(
    test_files / "words_bear.dialog.txt",
    "words.py"
)
def test_words2(): ...
