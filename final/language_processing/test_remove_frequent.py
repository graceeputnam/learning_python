from byu_pytest_utils import max_score, test_files, dialog

try:
    import remove_frequent


    @max_score(20)
    @dialog(
        test_files / "remove_frequent_1.expected.txt",
        "remove_frequent.py",
        4, test_files / "words_1.input.txt", "remove_frequent_1.observed.txt",
        output_file="remove_frequent_1.observed.txt"
    )
    def test_remove_frequent_1():
        ...


    @max_score(20)
    @dialog(
        test_files / "remove_frequent_2.expected.txt",
        "remove_frequent.py",
        2, test_files / "words_2.input.txt", "remove_frequent_2.observed.txt",
        output_file="remove_frequent_2.observed.txt"
    )
    def test_remove_frequent_2():
        ...


    @max_score(20)
    @dialog(
        test_files / "remove_frequent_3.expected.txt",
        "remove_frequent.py",
        5, test_files / "words_3.input.txt", "remove_frequent_3.observed.txt",
        output_file="remove_frequent_3.observed.txt"
    )
    def test_remove_frequent_3():
        ...


    @max_score(20)
    @dialog(
        test_files / "remove_frequent_4.expected.txt",
        "remove_frequent.py",
        6, test_files / "words_4.input.txt", "remove_frequent_4.observed.txt",
        output_file="remove_frequent_4.observed.txt"
    )
    def test_remove_frequent_4():
        ...


    @max_score(20)
    @dialog(
        test_files / "remove_frequent_5.expected.txt",
        "remove_frequent.py",
        100, test_files / "words_5.input.txt", "remove_frequent_5.observed.txt",
        output_file="remove_frequent_5.observed.txt"
    )
    def test_remove_frequent_5():
        ...

except ImportError:
    print('remove_frequent.py not submitted')
