from circuit_solver import CircuitSolver


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
    assert CircuitSolver("!!A").get_value()
    assert not CircuitSolver("!!!A").get_value()
    assert CircuitSolver("!!AB").get_value()
    assert CircuitSolver("!!A!B").get_value()


def test_and():
    assert CircuitSolver("AB").get_value()


def test_not_ands():
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
    assert CircuitSolver("!A+B").get_value()
    assert CircuitSolver("A+!B").get_value()
    assert not CircuitSolver("!A+!B").get_value()


def test_and_or_combos():
    assert CircuitSolver("AB+C").get_value()
    assert CircuitSolver("!AB+C").get_value()
    assert not CircuitSolver("!AB+!C").get_value()
    assert not CircuitSolver("A!B+!C").get_value()
    assert CircuitSolver("A+BC").get_value()
    assert CircuitSolver("A+!BC").get_value()
    assert CircuitSolver("!A+BC").get_value()
    assert not CircuitSolver("!A+!BC").get_value()


def test_multiply_star():
    assert CircuitSolver("A*B").get_value()
    assert not CircuitSolver("!A*B").get_value()
    assert CircuitSolver("A*B*C").get_value()
    assert not CircuitSolver("!A*B*C").get_value()
    assert not CircuitSolver("A*B*!C").get_value()


def test_multiply_star_combos():
    assert CircuitSolver("A*B+C").get_value()
    # assert CircuitSolver("!A*B+C").get_value()
    assert not CircuitSolver("!A*B+!C").get_value()
    assert not CircuitSolver("!A*B*C+D").get_value()
    # assert not CircuitSolver("D+A*B*!C").get_value()
