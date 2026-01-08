from circuit_solver import CircuitSolver, valid_string, format_string


def test_valid_strings():
    assert valid_string("AB")
    assert valid_string("A+B")
    assert valid_string("A + B")
    assert valid_string("(A + B) \n")
    assert valid_string("(A + B) + C")
    assert valid_string("!A")
    assert valid_string("!Ø+Å")
    assert valid_string("AxB")
    assert valid_string("A^B")


def test_invalid_strings():
    assert not valid_string("A-B")
    assert not valid_string("!")
    assert not valid_string(" ")
    assert not valid_string("")
    assert not valid_string("(")
    assert not valid_string("( ()")


def test_format_string():
    assert format_string("AB") == "AB"
    assert format_string("ab") == "AB"
    assert format_string(" a b \n") == "AB"


def test_string_arg():
    for arg in ("AB", "A+B"):
        cir_solv = CircuitSolver(arg)
        assert cir_solv._cir_string == arg


def test_and():
    assert CircuitSolver("AB").get_value()


def test_or():
    assert CircuitSolver("A+B").get_value()


def test_not():
    return  # TODO
    s_not = "!A"

    cir_solv = CircuitSolver(s_not)
    assert not cir_solv.get_value()
