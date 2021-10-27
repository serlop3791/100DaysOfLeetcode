import string
my_abc = list(string.ascii_lowercase)

# for c in my_abc:
#     print(ord(c))
#     code_point = ord(c)
#     # print(c)
#     print(chr(code_point))

test_one = 1234
test_two = 2356

# 0101 -> "0101"
def to_str(input_int):
    while input_int > 0:
        print(input_int)
        no_flooring = input_int / 10
        print("no_flooring: " + str(no_flooring))
        input_int //= 10

# to_str(2001)

def str_to_int(some_str):
    # "1001" -> 1001
    # ord, char
    for c in some_str[::-1]:
        print(ord(c))

str_to_int("2001")