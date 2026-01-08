from typing import Literal
from string import ascii_uppercase

# using all caps is Python convention for declaring a "constant"
# it's just like using "_" for a private variable. we just close our eyes and pretend :)

# removing "X" as I'm going to have the user type it for an XOR gate
NOR_LETTERS = ascii_uppercase.replace("X", "") + "ÆØÅ"

VALID_CHARS = NOR_LETTERS + "()*+!X \n"


def validate_string(string: str) -> bool:
    # empty string
    if not string:
        return False

    # invalid char in string
    for char in set(string):
        if char not in VALID_CHARS:
            return False

    # string is one char, and is not a letter
    if len(string) == 1 and string not in NOR_LETTERS:
        return False

    # depth of parenthesis is not matching
    if not string.count("(") == string.count(")"):
        return False

    return True


def format_string(string: str) -> str:
    string = string.upper()
    string = string.replace(" ", "")
    string = string.replace("\n", "")
    return string


class CircuitSolver:
    def __init__(self, circuit_string: str) -> None:
        self._cir_string = circuit_string.upper()
        self._invert = False
        self._operation: Literal["and", "or", "xor"]

        # condition for a leaf. should be a single character (excluding "X")
        if len(self._cir_string) == 1:
            if self._cir_string in NOR_LETTERS:
                return
            else:
                raise ValueError

        if self._cir_string[0] == "!":
            self._invert = True

        # TODO this is only for ending nodes
        if "+" in self._cir_string:
            self._operation = "or"
        else:
            self._operation = "and"

        self._right = CircuitSolver("A")
        self._left = CircuitSolver("B")

    def get_value(self) -> bool:
        if len(self._cir_string) == 1:
            return True

        left = self._left.get_value()
        right = self._right.get_value()

        match self._operation:
            case "and":
                value = left and right
            case "or":
                value = left or right
            case "xor":
                raise NotImplementedError
            case _:
                raise ValueError

        if self._invert:
            value = not value

        return value


# NOTE i need to handle inversion for each bool. should use something other than empty string?
