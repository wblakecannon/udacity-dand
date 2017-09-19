# todo: define a function named `population_density` that takes two arguments, 
# `population` and `land_area` (in square kilometres), and returns a population 
# density calculated from those values.

# Your code goes here!
def population_density(population, land_area):
    return population / land_area



# Here are test cases to verify that your function works as expected:
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}..., actual result: {}".format(expected_result2, test2))

