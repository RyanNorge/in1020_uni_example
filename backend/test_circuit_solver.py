from circuit_solver import CircuitSolver, validate_string, format_string

s_blank = ""
s_and = "AB"
s_or = "A+B"
s_not = "!A"


def test_valid_strings():
    assert validate_string("AB")
    assert validate_string("A+B")
    assert validate_string("A + B")
    assert validate_string("(A + B) \n")
    assert validate_string("(A + B) + C")
    assert validate_string("!A")
    assert validate_string("!Ø+Å")


def test_invalid_strings():
    assert not validate_string("A-B")
    assert not validate_string("!")
    assert not validate_string(" ")
    assert not validate_string("")
    assert not validate_string("(")
    assert not validate_string("( ()")


def test_format_string():
    assert format_string("AB") == "AB"
    assert format_string("ab") == "AB"
    assert format_string(" a b \n") == "AB"


def test_string_arg():
    for arg in (s_and, s_or):
        cir_solv = CircuitSolver(arg)
        assert cir_solv._cir_string == arg


def test_blank():
    return
    cir_solv = CircuitSolver(s_blank)
    assert cir_solv.get_value()


def test_and():
    cir_solv = CircuitSolver(s_and)
    assert cir_solv.get_value()


def test_or():
    cir_solv = CircuitSolver(s_or)
    assert cir_solv.get_value()


def test_not():
    return  # TODO
    cir_solv = CircuitSolver(s_not)
    assert not cir_solv.get_value()
