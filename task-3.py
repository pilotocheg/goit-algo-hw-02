from collections import deque

brackets = {
    # open brackets as keys and their symmetric close brackets as values
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
}


def is_symmetric(string: str) -> bool:
    stack = deque()
    open_brackets = brackets.keys()
    close_brackets = brackets.values()

    for char in string:
        if char in open_brackets:
            stack.append(char)

        elif char in close_brackets:
            if len(stack) == 0:
                return False

            last_open_bracket = stack.pop()
            symmetric_close_bracket = brackets[last_open_bracket]

            if char != symmetric_close_bracket:
                return False

    return len(stack) == 0
