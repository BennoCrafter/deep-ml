def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    scores = []

    for a_1 in a:
        s = []

        for a_2, b_2 in zip(a_1, b):
            if len(a_1) != len(b):
                return -1
            s.append(a_2 * b_2)

        scores.append(sum(s))

    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    return scores