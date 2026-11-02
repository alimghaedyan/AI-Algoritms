def minimax(depth, is_max):
    scores = [3, 5, 2, 9]

    if depth == 2:
        return scores.pop(0)

    if is_max:
        return max(
            minimax(depth + 1, False)
            for _ in range(2)
        )

    return min(
        minimax(depth + 1, True)
        for _ in range(2)
    )