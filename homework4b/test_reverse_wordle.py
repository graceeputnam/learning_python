from byu_pytest_utils import max_score, dialog, test_files


@max_score(3)
@dialog(
    test_files / 'reverse_wordle.dialog.txt', 'reverse_wordle.py'
)
def test_reverse_wordle(): ...


@max_score(3)
@dialog(
    test_files / 'reverse_wordle2.dialog.txt', 'reverse_wordle.py'
)
def test_reverse_wordle2(): ...
