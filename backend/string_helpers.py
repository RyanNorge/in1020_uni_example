from string import ascii_uppercase

# using all caps is Python convention for declaring a "constant"
# it's just like using "_" for a private variable. we just close our eyes and pretend :)

# removing "X" as I'm going to have the user type it for an XOR gate
NOR_LETTERS = ascii_uppercase.replace("X", "") + "ÆØÅ"

VALID_CHARS = NOR_LETTERS + "()*+!xX^ \n"


def valid_string(string: str) -> bool:
    """Returns whether a string has valid chars for the tree. Does not format the string."""

    string = string.strip()

    # empty string
    if not string:
        return False

    # invalid char in string
    for char in set(string):
        if char not in VALID_CHARS:
            return False

    # first char is an invalid operator
    if string[0] in "*+xX^":
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
