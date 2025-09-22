from byu_pytest_utils import max_score, dialog, test_files


@max_score(1)
@dialog(test_files / "only_o.dialog.txt","only_o.py")
def test_only_o(): ...


@max_score(1)
@dialog(test_files / "only_o2.dialog.txt","only_o.py")
def test_only_o_again(): ...
