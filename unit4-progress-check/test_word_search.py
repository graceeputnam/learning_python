from byu_pytest_utils import dialog, max_score, test_files


@max_score(15)
@dialog(test_files / "1Nephi.compass.dialog.txt",
        "word_search.py", test_files / "1Nephi.txt", "compass")
def test_compass(): ...


@max_score(15)
@dialog(test_files / "1Nephi.instruct.dialog.txt",
        "word_search.py", test_files / "1Nephi.txt", "instruct")
def test_instruct(): ...


@max_score(20)
@dialog(test_files / "1Nephi.foobar.dialog.txt",
        "word_search.py", test_files / "1Nephi.txt", "foobar")
def test_foobar(): ...
