import time
import timeit
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


# power_sum calcutates sum of random no of arguments with various data type


# def power_sum(*args):
#     sum = 0              # sum variable stores the value of addition till the current iterator
#     for arg in args:
#         # calling golbal_sum function with argument as sum till now and the new arguments that neend to be added
#         sum = sum_global(sum, arg)
#         # store this returned value in sum
#     return sum


# def sum_global(a, b):
#     sum = 0
#     if type(a) == list:
#         for i in a:
#             sum += i
#     elif type(a) == dict:
#         for i in a.values():
#             sum += i
#     else:
#         sum += a

#     if type(b) == list:
#         for i in b:
#             sum += i
#     elif type(b) == dict:
#         for i in b.values():
#             sum += i
#     else:
#         sum += b

#     return sum


# # Section 1 only integers were passed as argument
# print(True if sum_global(2, 3) == 5 else False)
# print(True if sum_global(-2, 3) == 1 else False)
# print(True if sum_global(-2, -3) == -5 else False)


# # Section 2 list or int ibject is passed as argument
# print(True if sum_global([1, 2], [2, 3]) == 8 else False)
# print(True if sum_global([1, 2], 2) == 5 else False)
# print(True if sum_global(1, 2) == 3 else False)
# print(True if sum_global(3, [2, 3]) == 8 else False)

# # Section 3 : sum Function with dict
# print(True if sum_global({"a": 1, "b": 2}, {"a": 2, "b": 3}) == 8 else False)
# print(True if sum_global({"a": 1, "b": 2}, 2) == 5 else False)
# print(True if sum_global(3, {"a": 2, "b": 3}) == 8 else False)


# # Section 4: sum Function with random no of arguments of any data type

# # sub section 1: Create test cases
# print(True if power_sum([1, 2], 2, {"a": 1, "b": 2}) == 8 else False)
# print(True if power_sum([1, 2], [2, 4], {"a": 1, "b": 2}) == 12 else False)
# print(True if power_sum(3, 2, {"a": 1, "b": 2}) == 8 else False)
# print(True if power_sum([1, 2], 2, 3) == 8 else False)
# print(True if power_sum(3, 2, 4, 5) == 14 else False)
# print(True if power_sum([1, 2], {"a": 2, "b": 3}, {
#       "a": 1, "b": 2}) == 11 else False)

# # sub section 2: think an approach
# # 1) Create a function Power_sum which takes *argvs as arguments
# # 2) Create a variable sum which holds the sum till the iterator
# # 3) For every arg in argvs call function global_sum with sum till now and current arg
# # 4) Store the value of global_sum in sum denoting the sum till now
# # 5) finally return sum


# # sub section 3: implementation
# # line NO. 6


# # test cases
# # print(True if power_sum([1, 2], 2, {"a": 1, "b": 2}) == 8 else False)
# # print(True if power_sum([1, 2], [2, 4], {"a": 1, "b": 2}) == 12 else False)
# # print(True if power_sum(3, 2, {"a": 1, "b": 2}) == 8 else False)
# # print(True if power_sum([1, 2], 2, 3) == 8 else False)
# # print(True if power_sum(3, 2, 4, 5) == 14 else False)
# # print(True if power_sum([1, 2], {"a": 2, "b": 3}, {
# #       "a": 1, "b": 2}) == 11 else False)


sum_speed = timeit.timeit('''l = [i for i in range(15000)]

sum(l)''', number=1)


power_sum_speed = timeit.timeit('''l = [i for i in range(15000)]

def power_sum(*args):
    sum=0
    for arg in args:
        sum = sum_global(sum, arg)
    return sum


def sum_global(a, b):
    sum = 0
    if type(a) == list:
        for i in a:
            sum += i
    elif type(a) == dict:
        for i in a.values():
            sum += i
    else:
        sum += a

    if type(b) == list:
        for i in b:
            sum += i
    elif type(b) == dict:
        for i in b.values():
            sum += i
    else:
        sum += b

    return sum


power_sum(l)''',  number=1)

sum_speed = "{:.4f}".format(sum_speed)
power_sum_speed = "{:.4f}".format(power_sum_speed)


print(f"speed of sum Function inbuilt python module ={sum_speed}")
print(f"speed of sum Function we built ={power_sum_speed}")
