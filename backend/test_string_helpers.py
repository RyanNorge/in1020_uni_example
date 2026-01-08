from string_helpers import valid_string, format_string


def test_valid_strings():
    assert valid_string("AB")
    assert valid_string("A+B")
    assert valid_string("A + B")
    assert valid_string("(A + B) \n")
    assert valid_string("(A + B) + C")
    assert valid_string("!A")
    assert valid_string("AxB")
    assert valid_string("A^B")
    assert valid_string("(A^B)+!(C+D)")


def test_norwegian_chars():
    assert valid_string("ÆØ+Å")
    assert valid_string("!Ø+Å")


def test_invalid_strings():
    assert not valid_string("A-B")
    assert not valid_string("!")
    assert not valid_string(" ")
    assert not valid_string("")
    assert not valid_string("(")
    assert not valid_string("( ()")


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
