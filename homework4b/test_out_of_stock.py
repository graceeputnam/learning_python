from byu_pytest_utils import max_score, dialog, test_files


@max_score(4)
@dialog(
    test_files / 'out_of_stock.dialog.txt',
    'out_of_stock.py'
)
def test_out_of_stock(): ...


@max_score(4)
@dialog(
    test_files / 'out_of_stock2.dialog.txt',
    'out_of_stock.py'
)
def test_out_of_stock2(): ...
