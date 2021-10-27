test_str = "here we go welcome to disneyland"

vowels = {'a', 'e', 'i', 'o', 'u'}


def iterative_counting(my_str):
    count = 0
    for c in my_str:
        if c.lower() not in vowels:
            count += 1
    return count


def recursive_counting(my_str, count=0):
    if len(my_str) == 0:
        return count
    c = my_str[0]
    if c.lower() not in vowels:
        count += 1
    return recursive_counting(my_str[1:], count)


print(recursive_counting(test_str, 0))
print(iterative_counting(test_str))
