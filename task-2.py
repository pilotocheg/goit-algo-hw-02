from collections import deque


def is_pallindrome(sentence: str) -> bool:
    chars_que = deque([char.lower() for char in sentence if char != " "])

    if len(chars_que) == 0:
        return True

    while len(chars_que):
        start_char = chars_que.popleft()

        if len(chars_que) == 0:
            return True

        end_char = chars_que.pop()

        if start_char != end_char:
            return False

    return True
