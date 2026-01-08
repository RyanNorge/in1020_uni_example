from circuit_solver import CircuitSolver

s_blank = ""
s_and = "AB"


def test_string_arg():
    for arg in (s_and, s_blank):
        cir_solv = CircuitSolver(arg)
        assert cir_solv._cir_string == arg


def test_blank():
    cir_solv = CircuitSolver(s_blank)
    assert cir_solv.get_value()


def test_and():
    cir_solv = CircuitSolver(s_and)
    assert cir_solv.get_value()
