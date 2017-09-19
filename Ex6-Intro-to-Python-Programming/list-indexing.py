"""
Quiz: List Indexing
Complete this function, how_many_days, that takes as its input a number representing the month, and
returns how many days are in that month. The days_in_month function that we've defined for you is a
list of how many days are in each month. For example, days_in_month(8) should return 31 because the
eighth month, August, has 31 days.

Remember to account for zero-based indexing!
def how_many_days(month_number):
    Returns the number of days in a month.
    WARNING: This function doesn't account for leap years!
    
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    #todo: return the correct value
    
# This test case should print 31, the number of days in the eighth month, August
print(how_many_days(8))
"""
def how_many_days(month_number):
    """Returns the number of days in a month.
    WARNING: This function doesn't account for leap years!
    """
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    return days_in_month[month_number-1]
    
# This test case should print 31, the number of days in the eighth month, August
print(how_many_days(8))