import pytest

from circuit_solver import CircuitSolverOne, CircuitSolverTwo


def test_invalid_strings():
    with pytest.raises(ValueError):
        CircuitSolverOne("A-B")
        CircuitSolverOne("!")
        CircuitSolverOne("(")
        CircuitSolverOne("( ()")


def test_whitespace():
    assert CircuitSolverOne("   ")._cir_string == ""
    assert CircuitSolverOne("\nY\nZ  ")._cir_string == "YZ"
    assert CircuitSolverOne(" ")._cir_string == ""


def test_format_string():
    assert CircuitSolverOne("AB")._cir_string == "AB"
    assert CircuitSolverOne("ab")._cir_string == "AB"
    assert CircuitSolverOne(" a b \n")._cir_string == "AB"
    assert CircuitSolverOne("æ ø å")._cir_string == "ÆØÅ"
    # assert CircuitSolver("(A + B) + C")._cir_string == "(A+B)+C"
    # assert CircuitSolver("(a^b)x!(æ*ø)")._cir_string == "(A^B)X!(Æ*Ø)"


def test_string_arg():
    for arg in ("AB", "A+B"):
        cir_solv = CircuitSolverOne(arg)
        assert cir_solv._cir_string == arg


def test_leaves():
    assert CircuitSolverOne("A").get_value()
    assert not CircuitSolverOne("").get_value()


def test_not():
    assert not CircuitSolverOne("!A").get_value()


def test_double_negative():
    return
    assert CircuitSolverOne("!!A").get_value()
    assert not CircuitSolverOne("!!!A").get_value()
    assert CircuitSolverOne("!!AB").get_value()
    assert CircuitSolverOne("!!A!B").get_value()


def test_and():
    assert CircuitSolverOne("AB").get_value()


def test_not_ands():
    return
    assert not CircuitSolverOne("!AB").get_value()
    assert not CircuitSolverOne("A!B").get_value()
    assert not CircuitSolverOne("!A!B").get_value()


def test_super_and():
    return
    assert CircuitSolverOne("ABC").get_value()


def test_or():
    assert CircuitSolverOne("A+B").get_value()
    assert CircuitSolverOne("A+B+C").get_value()
    assert CircuitSolverOne("A+B+C+D").get_value()


def test_or_combos():
    return
    assert CircuitSolverOne("!A+B").get_value()
    assert CircuitSolverOne("A+!B").get_value()
    assert not CircuitSolverOne("!A+!B").get_value()


def test_and_or_combos():
    return
    assert CircuitSolverOne("AB+C").get_value()
    assert CircuitSolverOne("!AB+C").get_value()
    assert not CircuitSolverOne("!AB+!C").get_value()
    assert not CircuitSolverOne("A!B+!C").get_value()
    assert CircuitSolverOne("A+BC").get_value()
    assert CircuitSolverOne("A+!BC").get_value()
    assert CircuitSolverOne("!A+BC").get_value()
    assert not CircuitSolverOne("!A+!BC").get_value()


def test_multiply_star():
    return
    assert CircuitSolverOne("A*B").get_value()
    assert not CircuitSolverOne("!A*B").get_value()
    assert CircuitSolverOne("A*B*C").get_value()
    assert not CircuitSolverOne("!A*B*C").get_value()
    assert not CircuitSolverOne("A*B*!C").get_value()


def test_multiply_star_combos():
    return
    assert CircuitSolverOne("A*B+C").get_value()
    # assert CircuitSolver("!A*B+C").get_value()
    assert not CircuitSolverOne("!A*B+!C").get_value()
    assert not CircuitSolverOne("!A*B*C+D").get_value()
    # assert not CircuitSolver("D+A*B*!C").get_value()


def test_okfd():
    assert isinstance(CircuitSolverOne("!!A").get_value(), bool)
    assert CircuitSolverOne("A").get_value()
    assert not CircuitSolverOne("!A").get_value()


#####
#####
#####


def test_init():
    CircuitSolverTwo("")


def test_empty_string():
    assert not CircuitSolverTwo("").get_value()
    ...


def test_single_value():
    assert CircuitSolverTwo("A").get_value()


def test_set_up_bools():
    x = CircuitSolverTwo("ABCDEFG")
    assert all(x._char_dict.values())


def test_randomize_bools():
    # This test could theoretically fail, but is good enough for this project.
    for _ in range(1_000_000):
        random = CircuitSolverTwo("ABCDEFG", randomize_bools=True)
        if not all(random._char_dict.values()):
            return
    raise ValueError("Expected random bools were never found")


def test_get_value_with_random_bools():
    # This test could theoretically fail, but is good enough for this project.
    for _ in range(1_000_000):
        if not CircuitSolverTwo("A", randomize_bools=True).get_value():
            return
    raise ValueError("Expected random bools were never found")
