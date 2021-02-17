def big_size(num_list):
    for idx in range(len(num_list)):
        if num_list[idx] > 0:
            num_list[idx] = "big"
    return num_list
print(big_size([-4,21,10,3,-1]))


def count_positives(lst):
    count = 0
    for x in lst:
        if x > 0:
            count += 1
    lst [len(lst)- 1] = count
    return lst
print(count_positives([-3,4,-6,3,4,6,4]))


list1 = [21,10,16,23]
total = sum(list1)
print("Sum of all elements in given list: ", total)


def Average(l):
    avg = sum(l) / len (l)
    return avg


my_list = [3,6,9,12,15]
average = Average(my_list)
print("Average of my_list: ", average)


len_list = [2,3,5,32,4,3,4,5,2]
print("Number of items in the list = ", len(len_list))


list1 = [4,43,56,3,33,-2]
print("Smallest element is: ", min(list1))


list1 = [4,43,56,3,33,-2]
print("largest element is: ", max(list1))


ult_list = [1, 2, 3]

sum = sum(ult_list)

max = max(ult_list)

length = len(ult_list)

average = sum/length


print(average)
print(max)
print(length)
print(sum)


def Reverse(lst): 
    lst.reverse() 
    return lst     
lst = [21, 11, 31, 71, 92] 
print(Reverse(lst))