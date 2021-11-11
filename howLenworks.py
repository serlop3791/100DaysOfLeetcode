
test_list = [1, 2, 3, 4, 5, 6, 7]
number_to_find = 6

def linear_search(data, target):
    length = len(data)
    print(length)
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

linear_search(test_list, number_to_find)