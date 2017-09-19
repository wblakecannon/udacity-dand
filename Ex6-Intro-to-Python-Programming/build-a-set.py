'''
Quiz: Build a Set
In a similar way to building an empty list with my_list = [], you can create an empty set with
my_set = set(). Using this technique, and the add method, build a set of all of the square numbers
greater than 0 and less than 2,000. For reference, I included my implementation of nearest_square
function from an earlier quiz. You may call the function in your code, integrate it into your code,
or ignore it altogether.
'''
squares = set()
n = 1
while n**2 < 2000:
    squares.add(n**2)
    n += 1
print(sorted(squares))
