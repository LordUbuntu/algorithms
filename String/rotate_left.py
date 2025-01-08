# Jacobus Burger (2025-01-08)
# Rotates a string leftways


def rotate(s: str, n: int) -> str:
    rot = list(s)
    for _ in range(n):
        # insert the rightmost element on the left side to rotate left
        rot.insert(0, rot.pop())
    return ''.join(rot)
