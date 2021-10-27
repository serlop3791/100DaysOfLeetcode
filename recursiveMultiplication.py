def recursive_multiply(x, y):
    if x == 0:
        return 0
    return y + recursive_multiply(x - 1, y)


print(recursive_multiply(3, 2))
# 2 + 2 + 2 + 2