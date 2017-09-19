'''
Quiz: Median
The function in this quiz, median, returns the median value of an input list. Unfortunately it only
works with lists that have an odd number of elements. Modify the function so that when median is
given a list with an even number of elements, it returns the mean of the two central elements. The
provided test cases demonstrate the expected behavior.
'''
def median(numbers):
    if len(numbers) % 2 == 0:
        numbers.sort()
        low_num = int(len(numbers) / 2 - 1)
        high_num = int(len(numbers) / 2)
        return (numbers[low_num] + numbers[high_num]) / 2
    
    else:
        numbers.sort() #The sort method sorts a list directly, rather than returning a new sorted list
        middle_index = int(len(numbers)/2)
        return numbers[middle_index]

test1 = median([1,2,3])
print("expected result: 2, actual result: {}".format(test1))

test2 = median([1,2,3,4])
print("expected result: 2.5, actual result: {}".format(test2))

test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))

'''
Udacity Solution: Median
There are two cases the median function needs to handle: inputs with even lengths and inputs with odd lengths. I can use an if statement to determine whether the list's length is even or odd.

def median(numbers):
    numbers.sort() 
    if len(numbers) % 2:
        # if the list has an odd number of elements,
        # the median is the middle element
        middle_index = int(len(numbers)/2)
        return numbers[middle_index]
    else:
        # if the list has an even number of elements,
        # the median is the average of the middle two elements
        right_of_middle = len(numbers)//2 
        left_of_middle = right_of_middle - 1
        return (numbers[right_of_middle] + numbers[left_of_middle])/2
'''
