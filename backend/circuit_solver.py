from typing import Literal, Tuple
from string import ascii_uppercase

# using all caps is Python convention for declaring a "constant"
# it's just like using "_" for a private variable. we just close our eyes and pretend :)

# removing "X" as I'm going to have the user type it for an XOR gate
NOR_LETTERS = ascii_uppercase.replace("X", "") + "ÆØÅ"

VALID_CHARS = NOR_LETTERS + "()*+!xX^ \n"


class CircuitSolver:
    def __init__(self, circuit_string: str) -> None:
        self._cir_string = circuit_string
        self._value = None
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
                raise ValueError(f"Invalid string with {self._cir_string}")

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
                return True, char_two, "or", ""

        # TODO check for parenthesis
        "()"

        # pattern "!!...", "!(..."
        if string[0:2] in ("!!", "!("):
            return True, string[1:], "or", ""

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

        # pattern "...[operator]..."
        return False, left_side, operator, right_side

        if string[left_side_len] == "+":
            return False, left_side, "or", string[left_side_len + 1 :]

        raise NotImplementedError(
            f"Not implimented for string {string} with left_side {len(left_side)}"
        )

    def get_value(self) -> bool:
        """
        Returns the calculated boolean value of the node,
        as determined by its child nodes and inversion status.
        """

        # TODO move this to init
        # condition for a populated leaf
        if len(self._cir_string) == 1:
            return True

        # condition for an empty leaf
        if len(self._cir_string) == 0:
            return False

        if self._value is not None:
            return self._value

        #### things will break here...
        # self._left._evaluate(_stage="and", _branch=True)
        # self._right._evaluate(_stage="and", _branch=True)
        # self._left._evaluate(_stage="or", _branch=True)
        # self._right._evaluate(_stage="or", _branch=True)

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

        self._value = value

        return value

    def _evaluate(
        self, _stage: Literal["and", "or", None] = None, _branch=False
    ) -> None:
        # if called directly on root node for some reason
        if not _branch:
            return

        #### definately not done with stuff

        self._left._evaluate(_stage, _branch=True)
        self._right._evaluate(_stage, _branch=True)
