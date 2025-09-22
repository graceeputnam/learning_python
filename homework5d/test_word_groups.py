from byu_pytest_utils import max_score, test_files, dialog


@max_score(3)
@dialog(
    test_files/"words.dialog.txt",
    "word_groups.py", test_files/"words.txt"
)
def test_word_groups(): ...


@max_score(3)
@dialog(
    test_files/"words2.dialog.txt",
    "word_groups.py", test_files/"words2.txt"
)
def test_word_groups2(): ...
