from string_helpers import is_valid_string, format_string


def test_valid_strings():
    assert is_valid_string("AB")
    assert is_valid_string("A+B")
    assert is_valid_string("A + B")
    assert is_valid_string("(A + B) \n")
    assert is_valid_string("(A + B) + C")
    assert is_valid_string("!A")
    assert is_valid_string("AxB")
    assert is_valid_string("A^B")
    assert is_valid_string("(A^B)+!(C+D)")


def test_norwegian_chars():
    assert is_valid_string("ÆØ+Å")
    assert is_valid_string("!Ø+Å")


def test_invalid_strings():
    assert not is_valid_string("A-B")
    assert not is_valid_string("!")
    assert not is_valid_string(" ")
    assert not is_valid_string("")
    assert not is_valid_string("(")
    assert not is_valid_string("( ()")


def test_xor_char():
    assert format_string("x") == "X"


def test_whitespace():
    assert format_string("   ") == ""
    assert format_string("\nX\nY  ") == "XY"
    assert format_string(" ") == ""


def test_format_string():
    assert format_string("AB") == "AB"
    assert format_string("ab") == "AB"
    assert format_string(" a b \n") == "AB"
    assert format_string("(A + B) + C") == "(A+B)+C"
    assert format_string("(a^b)x!(æ*ø)") == "(A^B)X!(Æ*Ø)"
