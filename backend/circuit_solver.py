from typing import Literal, Tuple
from string import ascii_uppercase

from string_helpers import format_string, is_valid_string

# using all caps is Python convention for declaring a "constant"
# it's just like using "_" for a private variable. we just close our eyes and pretend :)

# removing "X" as I'm going to have the user type it for an XOR gate
NOR_LETTERS = ascii_uppercase.replace("X", "") + "ÆØÅ"

VALID_CHARS = NOR_LETTERS + "()*+!xX^ \n"


class CircuitSolver:
    def __init__(self, circuit_string: str, _is_root=True) -> None:
        self._value = None
        self._is_leaf = False
        self._is_root = _is_root

        self._cir_string: str
        self._invert: bool
        self._operation: Literal["and", "or", "xor"]
        self._left: CircuitSolver
        self._right: CircuitSolver

        circuit_string = format_string(circuit_string)

        if not is_valid_string(circuit_string):
            raise ValueError(f"Invalid string: {circuit_string}")

        self._cir_string = circuit_string

        # if a leaf, then set values and early return
        self._check_for_leaf()
        if self._is_leaf:
            return

        # get inversion status and args for child nodes
        invert, left_side, operator, right_side = self._parse_inversion_and_child_nodes(
            self._cir_string
        )

        self._invert = invert
        self._left = CircuitSolver(left_side, _is_root=False)
        self._operation = operator
        self._right = CircuitSolver(right_side, _is_root=False)

    def _check_for_leaf(self) -> None:
        """Check if node is a leaf, and set instance variables if it is"""

        # empty leaf is empty string
        if not self._cir_string:
            self._is_leaf = True
            if self._is_root:
                # root should return false on an empty string
                self._value = False
            else:
                # True on an empty string on a leaf.
                # This is so that an "and" operation will be evaluated on leaves
                # before any "or" operations are evaluated.
                self._value = True
            return

        # populated leaf is single char
        if len(self._cir_string) == 1:
            if self._cir_string in NOR_LETTERS:
                self._is_leaf = True
                self._value = True
                return
            else:
                raise ValueError(f"Invalid string with {self._cir_string}")

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

        # error if an empty string came in
        if not string:
            raise ValueError

        char_one = string[0]
        len_of_string = len(string)

        # error if first char is an invalid operator
        if char_one in "*+X^":
            raise ValueError(f"Invalid string with {string}")

        # we now know that the first char is either a letter or in ["!()"]

        # two chars
        if len_of_string == 2:
            char_two = string[1]

            char_one_is_letter = char_one in NOR_LETTERS
            char_two_is_letter = char_two in NOR_LETTERS

            # pattern "AB"
            if char_one_is_letter and char_two_is_letter:
                return False, char_one, "and", char_two

            # pattern "!A"
            if char_one == "!" and char_two_is_letter:
                return True, char_two, "and", ""

        # TODO check for parenthesis
        "()"

        # pattern "!!...", "!(..."
        if string[0:2] in ("!!", "!("):
            return True, string[1:], "and", ""

        # pattern "!AB[operator]...", "A!B[operator]...", "!A!B[operator]...", "ABC[operator]..."
        left_side = ""
        for char in string:
            # break when finding an operator or parenthesis
            if char in "()*+X^":
                break
            left_side += char

        # pattern "!AB", "A!B", "!A!B", "ABC"
        if left_side == string:
            if string[0] == "!":
                # do not return True for inversion here. it is applied to the next node.
                return False, string[0:2], "and", string[2:]
            else:
                return False, string[0:1], "and", string[1:]

        # from here on is pattern "...[operator]..."

        # get operator and string for right branch node
        left_side_len = len(left_side)
        operator_char = string[left_side_len]
        right_side = string[left_side_len + 1 :]

        match operator_char:
            case "+":
                operator = "or"
            case "*":
                operator = "and"
            case "^" | "X":
                operator = "xor"
            case _:
                raise ValueError(f"Invalid operator_char: {operator_char}")

        return False, left_side, operator, right_side

    def get_value(self) -> bool:
        """
        Returns the calculated boolean value of the node,
        as determined by its child nodes and inversion status.
        """

        # early return if value is already cached
        if self._value is not None:
            return self._value

        #### things will break here...
        self._left._evaluate(_stage="and")
        self._right._evaluate(_stage="and")
        self._left._evaluate(_stage="or")
        self._right._evaluate(_stage="or")

        ### okfd
        left = self._left._value
        right = self._right._value

        # return

        # get values from both child branches
        # left = self._left.get_value()
        # right = self._right.get_value()

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

        self._value = value

        return value

    def _evaluate(self, _stage: Literal["and", "or"]) -> None:
        # do not run if value already cached
        if self._value is not None:
            return

        #### definately not done with stuff

        # get values from both child branches
        left = self._left._value
        right = self._right._value

        if left is None:
            self._left._evaluate("and")
            self._left._evaluate("or")
            left = self._left._value

        if right is None:
            self._right._evaluate("and")
            self._right._evaluate("or")
            right = self._right._value

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

        self._value = value

        # self._left._evaluate(_stage)
        # self._right._evaluate(_stage)
