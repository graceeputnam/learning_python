from byu_pytest_utils import max_score, dialog, test_files


@max_score(2)
@dialog(test_files / "voting_one.dialog.txt", "voting.py", "Favorite Cereal")
def test_voting_one(): ...


@max_score(2)
@dialog(test_files / "voting_two.dialog.txt", "voting.py", "Favorite Candy")
def test_voting_two(): ...
