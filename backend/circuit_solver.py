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
        self._cir_string = circuit_string
        self._invert: bool
        self._operation: Literal["and", "or", "xor"]
        self._left: CircuitSolver
        self._right: CircuitSolver

        # condition for a leaf. should be an empty string or a single char
        if not self._cir_string:
            return
        if len(self._cir_string) == 1:
            if self._cir_string in NOR_LETTERS:
                return
            else:
                raise ValueError

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

        # error if an empty string came in
        if not string:
            raise ValueError

        len_of_string = len(string)

        # error if first char is an invalid operator
        if string[0] in "*+X^":
            raise ValueError

        # two chars
        if len_of_string == 2:
            char_one = string[0]
            char_two = string[1]

            char_one_is_letter = char_one in NOR_LETTERS
            char_two_is_letter = char_two in NOR_LETTERS

            # pattern "AB"
            if char_one_is_letter and char_two_is_letter:
                return False, char_one, "and", char_two

            # pattern "!A"
            if char_one == "!" and char_two_is_letter:
                return True, char_two, "or", ""

        # we now know that the first char is either a letter or in ["!()"]

        # TODO check for parenthesis
        "()"

        # TODO quick fix. not always true.
        # check to see if this node should be inverted
        if self._cir_string[0] == "!":
            invert = True

        # pattern "AB"
        left_side = ""
        for char in string:
            # break when finding an operator or parenthesis
            if char not in NOR_LETTERS or char == "!":
                break
            left_side += char

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
