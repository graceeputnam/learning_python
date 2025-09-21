from byu_pytest_utils import max_score, test_files, dialog

try:
    import analyze_logs


    @max_score(20)
    @dialog(
        test_files / "analyze_logs_1.dialog.txt",
        "analyze_logs.py",
        test_files / "ip_logs_1.txt"
    )
    def test_analyze_logs_1():
        ...


    @max_score(20)
    @dialog(
        test_files / "analyze_logs_2.dialog.txt",
        "analyze_logs.py",
        test_files / "ip_logs_2.txt"
    )
    def test_analyze_logs_2():
        ...


    @max_score(20)
    @dialog(
        test_files / "analyze_logs_3.dialog.txt",
        "analyze_logs.py",
        test_files / "ip_logs_3.txt"
    )
    def test_analyze_logs_3():
        ...


    @max_score(20)
    @dialog(
        test_files / "analyze_logs_4.dialog.txt",
        "analyze_logs.py",
        test_files / "ip_logs_4.txt"
    )
    def test_analyze_logs_4():
        ...


    @max_score(20)
    @dialog(
        test_files / "analyze_logs_5.dialog.txt",
        "analyze_logs.py",
        test_files / "ip_logs_5.txt"
    )
    def test_analyze_logs_5():
        ...

except ImportError:
    print('analyze_logs.py not submitted')
