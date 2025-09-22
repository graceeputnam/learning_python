from byu_pytest_utils import max_score, test_files, dialog


@max_score(3.5)
@dialog(
    test_files/"nba-groups.dialog.txt",
    "group_csv.py", test_files/"nba_players_short.csv", 5, 1
)
def test_group_csv(): ...


@max_score(3.5)
@dialog(
    test_files/"nba-groups2.dialog.txt",
    "group_csv.py", test_files/"nba_players_short.csv", 6, 2
)
def test_group_csv2(): ...
