from byu_pytest_utils import max_score, test_files, dialog


@max_score(7.5)
@dialog(
        test_files / "small.txt",
        "decode.py",
        test_files / "cipher.csv",
        test_files / "small.encoded.expected.txt",
        test_files / "small.decoded.observed.txt",
        output_file=test_files / "small.decoded.observed.txt"
    )
def test_decode_small(): ...


@max_score(7.5)
@dialog(
        test_files / "simple.txt",
        "decode.py",
        test_files / "cipher.csv",
        test_files / "simple.encoded.expected.txt",
        test_files / "simple.decoded.observed.txt",
        output_file=test_files / "simple.decoded.observed.txt"
    )
def test_decode_simple(): ...


@max_score(7.5)
@dialog(
        test_files / "message.txt",
        "decode.py",
        test_files / "cipher.csv",
        test_files / "message.encoded.expected.txt",
        test_files / "message.decoded.observed.txt",
        output_file=test_files / "message.decoded.observed.txt"
    )
def test_decode_message(): ...


@max_score(7.5)
@dialog(
        test_files / "1Nephi.v1.txt",
        "decode.py",
        test_files / "cipher.csv",
        test_files / "1Nephi.v1.encoded.expected.txt",
        test_files / "1Nephi.v1.decoded.observed.txt",
        output_file=test_files / "1Nephi.v1.decoded.observed.txt"
    )
def test_decode_nephi(): ...
