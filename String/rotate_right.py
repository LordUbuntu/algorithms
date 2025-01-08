# Jacobus Burger (2025-01-06)
# rotates a string by a certain amount


def rotate(s: str, n: int) -> str:
    rot = list(s)
    for _ in range(n):
        rot.append(rot.pop(0))
    return ''.join(rot)
