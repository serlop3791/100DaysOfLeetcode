str_1 = "lucidProgramming"
str_2 = "LucidProgramming"
str_3 = "lucidprogramming"


def iterativeFindUpper(testStr):
    for c in testStr:
        if c == c.upper():
            return c
    return None


# print(iterativeFindUpper(str_1))
# print(iterativeFindUpper(str_2))
# print(iterativeFindUpper(str_3))


def recursiveFindUpper(singleStr, testStr):
    # print(singleStr)
    if len(testStr) == 0:
        return None
    if singleStr != "" and singleStr == singleStr.upper():
        return singleStr

    return recursiveFindUpper(testStr[0:1], testStr[1:])

print(recursiveFindUpper("", str_1))

# print(recursiveFindUpper(str_2))
# print(recursiveFindUpper(str_3))
