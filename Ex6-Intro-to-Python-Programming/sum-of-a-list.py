'''
Quiz: Sum of a List
Define a function, list_sum, that takes a list as its argument and returns the sum of the elements
in the list. Use a for loop to iterate over the list
'''

def list_sum(input_list):
    sum = 0
    for element in input_list:
        sum += element
    return sum



#These test cases check the list_sum works correctly
test1 = list_sum([1, 2, 3])
print("expected result: 6, actual result: {}".format(test1))

test2 = list_sum([-1, 0, 1])
print("expected result: 0, actual result: {}".format(test2))