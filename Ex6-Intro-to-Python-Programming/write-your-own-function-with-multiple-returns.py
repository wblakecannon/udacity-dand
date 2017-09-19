'''Quiz: Write your own function with multiple returns
The cylinder_surface_area function calculates the surface area of cylinders that are solid or
hollow. The has_top_and_bottom argument is True or False depending on whether the cylinder is
solid or hollow. The surface area of a solid cylinder includes the areas of the top and bottom

Restructure this function definition so that it has two return statements in its body.
def cylinder_surface_area(radius, height, has_top_and_bottom):
    side_area = height * 6.28 * radius
    if has_top_and_bottom:
        top_area = 3.14 * radius ** 2
        side_area += 2 * top_area
    return side_area
'''
def cylinder_surface_area(radius, height, has_top_and_bottom):
    side_area = height * 6.28 * radius
    if has_top_and_bottom:
        top_area = 3.14 * radius ** 2
        side_area += 2 * top_area
        return side_area
    else:
        return side_area

print(cylinder_surface_area(3, 3, True))
print(cylinder_surface_area(3, 3, False))

'''Udacity solution:
def cylinder_surface_area(radius, height, has_top_and_bottom):
    side_area = height * 6.28 * radius
    if has_top_and_bottom:
        top_area = 3.14 * radius ** 2
        return top_area + side_area
    else:
        return side_area
