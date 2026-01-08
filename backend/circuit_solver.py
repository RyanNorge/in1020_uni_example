from typing import Literal, Tuple
from string import ascii_uppercase

# using all caps is Python convention for declaring a "constant"
# it's just like using "_" for a private variable. we just close our eyes and pretend :)

# removing "X" as I'm going to have the user type it for an XOR gate
NOR_LETTERS = ascii_uppercase.replace("X", "") + "ÆØÅ"

VALID_CHARS = NOR_LETTERS + "()*+!xX^ \n"


def valid_string(string: str) -> bool:
    """Returns whether a string has valid chars for the tree. Does not format the string."""
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
    """Formats a validated string to be passed into the CircuitSolver class."""
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

        # check to see if this node should be inverted
        if self._cir_string[0] == "!":
            self._invert = True

            # remove inversion char from the start of the string
            self._cir_string = self._cir_string[1:]

        # get inversion status and args for child nodes
        invert, left_side, operator, right_side = self._parse_inversion_and_child_nodes(
            self._cir_string
        )

        self._invert = invert
        self._right = CircuitSolver(left_side)
        self._operation = operator
        self._left = CircuitSolver(right_side)

    def _parse_inversion_and_child_nodes(
        self, string: str
    ) -> Tuple[bool, str, Literal["and", "or", "xor"], str]:
        """
        Parse the inversion of the current node and the args for the next nodes of the tree.

        Returns:
            bool: whether this node should be inverted
            str: arg for left branch node
            Literal['and', 'or', 'xor']: operator to be used between the two branches
            str: arg for rigth branch node
        """
        invert, left_side, operator, right_side = False, "A", "and", "B"

        # TODO check for parenthesis
        "()"

        # check to see if this node should be inverted
        if self._cir_string[0] == "!":
            invert = True

        char_one = string[0]
        if char_one not in NOR_LETTERS:
            raise ValueError

        char_two = string[1]

        # pattern "AB"
        if char_two in NOR_LETTERS:
            return invert, char_one, "and", char_two

        # TODO
        #
        "!"
        #
        "*"
        #
        "+"
        #
        "X^"
        # pattern "A*B"
        if char_two in "()*+!X^":
            ...

        return invert, left_side, operator, right_side

    def get_value(self) -> bool:
        """
        Returns the calculated boolean value of the node,
        as determined by its child nodes and inversion status.
        """
        # condition for a populated leaf
        if len(self._cir_string) == 1:
            return True

        # condition for an empty leaf
        if len(self._cir_string) == 0:
            return False

        # get values from both child branches
        left = self._left.get_value()
        right = self._right.get_value()

        # perform operation between branches
        match self._operation:
            case "and":
                value = left and right
            case "or":
                value = left or right
            case "xor":
                # TODO
                raise NotImplementedError
            case _:
                raise ValueError

        # invert if inversion was previously detected
        if self._invert:
            value = not value

        return value
