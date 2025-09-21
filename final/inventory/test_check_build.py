from byu_pytest_utils import max_score, test_files, dialog

try:
    import check_build


    @max_score(20)
    @dialog(
        test_files / "check_build_1.dialog.txt",
        "check_build.py",
        test_files / "inventory.csv",
        test_files / "build_1.csv"
    )
    def test_check_build_1():
        ...


    @max_score(20)
    @dialog(
        test_files / "check_build_2.dialog.txt",
        "check_build.py",
        test_files / "inventory.csv",
        test_files / "build_2.csv"
    )
    def test_check_build_2():
        ...


    @max_score(20)
    @dialog(
        test_files / "check_build_3.dialog.txt",
        "check_build.py",
        test_files / "inventory.csv",
        test_files / "build_3.csv"
    )
    def test_check_build_3():
        ...


    @max_score(20)
    @dialog(
        test_files / "check_build_4.dialog.txt",
        "check_build.py",
        test_files / "inventory.csv",
        test_files / "build_4.csv"
    )
    def test_check_build_4():
        ...


    @max_score(20)
    @dialog(
        test_files / "check_build_5.dialog.txt",
        "check_build.py",
        test_files / "inventory.csv",
        test_files / "build_5.csv"
    )
    def test_check_build_5():
        ...

except ImportError:
    print('check_build.py not submitted')
