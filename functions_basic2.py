def countdown(num):
    nums_list = []
    for val in range(num,-1,-1):
        nums_list.append(val)
    return nums_list
print(countdown(10))

def print_and_return(nums_list):
    print(nums_list[0])
    return nums_list[1]
print(print_and_return([3,5]))

def first_plus_length(nums_list):
    return nums_list[0] + len(nums_list)
print(first_plus_length([21,10,16,23,11]))

def values_greater_than_second(orig_list):
    first_list = []
    second_list = orig_list[1]
    for idx in range(len(orig_list)):
        if orig_list[idx] > second_list:
            first_list.append(orig_list[idx])
    print(len(first_list))
    return first_list
print(values_greater_than_second([7,3,5,4,2,8]))

def length_and_value(size, value):
    x = []
    for num_times in range(size):
        x.append(value)
    return x
print(length_and_value(10,21))
