import timeit

# power_sum calcutates sum of random no of arguments with various data type

def power_sum(*args):
    # sum variable stores the value of addition till the current iterator
    sum = 0
    for arg in args:                    # calling golbal_sum function with argument as sum till now and the new arguments that neend to be added
        sum = sum_global(sum, arg)      # store this returned value in sum
    return sum


# sum_golbal calculates the sum of two values a and b where a and b could be int, list, dict

def sum_global(a, b):
    sum = 0
    if type(a) == list:    # checks if a is list then runs the loop to add up all elements of list to sum
        for i in a:
            sum += i
    elif type(a) == dict:  # checks if a is dict then runs the loop to add up all values in key-value pair of dict to sum
        for i in a.values():
            sum += i
    else:                  # all int fall in this case and get added up to sum
        sum += a

    if type(b) == list:
        for i in b:
            sum += i
    elif type(b) == dict:
        for i in b.values():
            sum += i
    else:
        sum += b

    return sum            # return sum of a and b (irrespective of data type)


print("sum_global function on integers")
# Section 1 only integers are passed as argument
# test case
print(f"{True if sum_global(2, 3) == 5 else False}")
print(True if sum_global(-2, 3) == 1 else False)
print(True if sum_global(-2, -3) == -5 else False)
print()

print("sum_global function on integers and list")
# # Section 2 list or int ibject are passed as argument
# test case
print(True if sum_global([1, 2], [2, 3]) == 8 else False)
print(True if sum_global([1, 2], 2) == 5 else False)
print(True if sum_global(1, 2) == 3 else False)
print(True if sum_global(3, [2, 3]) == 8 else False)
print()


print("sum_global function on integers and dict")
# # Section 3 : dict or int ibject are passed as argument
# test case
print(True if sum_global({"a": 1, "b": 2}, {"a": 2, "b": 3}) == 8 else False)
print(True if sum_global({"a": 1, "b": 2}, 2) == 5 else False)
print(True if sum_global(3, {"a": 2, "b": 3}) == 8 else False)
print()


# # Section 4: sum Function with random no of arguments of any data type
print("power_sum function on n number of argument and different data type")

# # sub section 1: Create test cases
# test case
print(True if power_sum([1, 2], 2, {"a": 1, "b": 2}) == 8 else False)
print(True if power_sum([1, 2], [2, 4], {"a": 1, "b": 2}) == 12 else False)
print(True if power_sum(3, 2, {"a": 1, "b": 2}) == 8 else False)
print(True if power_sum([1, 2], 2, 3) == 8 else False)
print(True if power_sum(3, 2, 4, 5) == 14 else False)
print(True if power_sum([1, 2], {"a": 2, "b": 3}, {
      "a": 1, "b": 2}) == 11 else False)
print()

# sub section 2: think an approach
# 1) Create a function Power_sum which takes * argvs as arguments
# 2) Create a variable sum which holds the sum till the iterator
# 3) For every arg in argvs call function global_sum with sum till now and current arg
# 4) Store the value of global_sum in sum denoting the sum till now
# 5) finally return sum

# sub section 3: implementation
# line NO. 6

print()
# Benchmark of our power_sum() function on inbuilt sum() function of python
# performing generat addition of integers on input size of 15000
print("Benchmark power_sum function and sum function of python module:-")

# Running time test on sum()

# timeit.timeit function takes two argument :-
# 1) Code snippet whose run time is to be recorded
# 2) number implies number of times the test has to be performed on input set
sum_speed = timeit.timeit('''l = [i for i in range(15000)]                  

sum(l)''', number=1)

# Running time test on power_sum()

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

# formatting Results upto 4 decimal places
print()
sum_speed = "{:.4f}".format(sum_speed)
power_sum_speed = "{:.4f}".format(power_sum_speed)

# Showing results
print(f"speed of sum Function inbuilt python module ={sum_speed}")
print(f"speed of sum Function we built ={power_sum_speed}")
