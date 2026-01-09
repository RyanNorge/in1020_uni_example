import pytest

from circuit_solver import CircuitSolver


def test_invalid_strings():
    with pytest.raises(ValueError):
        CircuitSolver("A-B")
        CircuitSolver("!")
        CircuitSolver("(")
        CircuitSolver("( ()")


def test_whitespace():
    assert CircuitSolver("   ")._cir_string == ""
    assert CircuitSolver("\nY\nZ  ")._cir_string == "YZ"
    assert CircuitSolver(" ")._cir_string == ""


def test_format_string():
    assert CircuitSolver("AB")._cir_string == "AB"
    assert CircuitSolver("ab")._cir_string == "AB"
    assert CircuitSolver(" a b \n")._cir_string == "AB"
    assert CircuitSolver("æ ø å")._cir_string == "ÆØÅ"
    # assert CircuitSolver("(A + B) + C")._cir_string == "(A+B)+C"
    # assert CircuitSolver("(a^b)x!(æ*ø)")._cir_string == "(A^B)X!(Æ*Ø)"


def test_string_arg():
    for arg in ("AB", "A+B"):
        cir_solv = CircuitSolver(arg)
        assert cir_solv._cir_string == arg


def test_leaves():
    assert CircuitSolver("A").get_value()
    assert not CircuitSolver("").get_value()


def test_not():
    assert not CircuitSolver("!A").get_value()


def test_double_negative():
    return
    assert CircuitSolver("!!A").get_value()
    assert not CircuitSolver("!!!A").get_value()
    assert CircuitSolver("!!AB").get_value()
    assert CircuitSolver("!!A!B").get_value()


def test_and():
    assert CircuitSolver("AB").get_value()


def test_not_ands():
    return
    assert not CircuitSolver("!AB").get_value()
    assert not CircuitSolver("A!B").get_value()
    assert not CircuitSolver("!A!B").get_value()


def test_super_and():
    assert CircuitSolver("ABC").get_value()


def test_or():
    assert CircuitSolver("A+B").get_value()
    assert CircuitSolver("A+B+C").get_value()
    assert CircuitSolver("A+B+C+D").get_value()


def test_or_combos():
    return
    assert CircuitSolver("!A+B").get_value()
    assert CircuitSolver("A+!B").get_value()
    assert not CircuitSolver("!A+!B").get_value()


def test_and_or_combos():
    return
    assert CircuitSolver("AB+C").get_value()
    assert CircuitSolver("!AB+C").get_value()
    assert not CircuitSolver("!AB+!C").get_value()
    assert not CircuitSolver("A!B+!C").get_value()
    assert CircuitSolver("A+BC").get_value()
    assert CircuitSolver("A+!BC").get_value()
    assert CircuitSolver("!A+BC").get_value()
    assert not CircuitSolver("!A+!BC").get_value()


def test_multiply_star():
    return
    assert CircuitSolver("A*B").get_value()
    assert not CircuitSolver("!A*B").get_value()
    assert CircuitSolver("A*B*C").get_value()
    assert not CircuitSolver("!A*B*C").get_value()
    assert not CircuitSolver("A*B*!C").get_value()


def test_multiply_star_combos():
    return
    assert CircuitSolver("A*B+C").get_value()
    # assert CircuitSolver("!A*B+C").get_value()
    assert not CircuitSolver("!A*B+!C").get_value()
    assert not CircuitSolver("!A*B*C+D").get_value()
    # assert not CircuitSolver("D+A*B*!C").get_value()


def test_okfd():
    assert isinstance(CircuitSolver("!!A").get_value(), bool)
    assert CircuitSolver("A").get_value()
    assert not CircuitSolver("!A").get_value()
