from byu_pytest_utils import dialog, max_score, test_files


@max_score(25)
@dialog(test_files / "1Nephi.45.dialog.txt",
        "notable_words.py", test_files / "1Nephi.txt", "45")
def test_45(): ...


@max_score(25)
@dialog(test_files / "1Nephi.27.dialog.txt",
        "notable_words.py", test_files / "1Nephi.txt", "27")
def test_27(): ...
