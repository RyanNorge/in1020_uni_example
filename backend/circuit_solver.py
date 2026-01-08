class CircuitSolver:
    def __init__(self, circuit_string: str) -> None:
        self._cir_string = circuit_string
        self._operation: str | None = None

        if self._cir_string == "":
            return

        if self._cir_string:
            # TODO
            self._operation = "and"

        self._right = CircuitSolver("")
        self._left = CircuitSolver("")

    def get_value(self) -> bool:
        if self._cir_string == "":
            return True

        left = self._left.get_value()
        right = self._right.get_value()

        match self._operation:
            case "and":
                return left and right
            case "or":
                return left or right
            # case "not":
            #     ...
