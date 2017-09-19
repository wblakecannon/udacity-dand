'''
Quiz: Days and Hours
Try your hand at writing a function that uses a tuple to return multiple values. Write an hours2days function that takes one argument, an integer, that is a time period in hours. The function should return a tuple of how long that period is in days and hours, with hours being the remainder that can't be expressed in days. For example, 39 hours is 1 day and 15 hours, so the function should return (1,15).

These examples demonstrate how the function can be used:

>>> hours2days(24) # 24 hours is one day and zero hours
(1, 0)
>>> hours2days(25) # 25 hours is one day and one hour
(1, 1)
>>> hours2days(10000)
(416, 16)
'''
def hours2days(hours):
    days, hours = (hours / 24), (hours % 24)
    return int(days), int(hours)

print(hours2days(24))
print(hours2days(25))
print(hours2days(10000))

'''
Udacity Solution:

def hours2days(input_hours):
    days = input_hours // 24
    hours = input_hours % 24
    return days, hours
'''