# Write a program that tests if two rectangles have a nonempty intersection.
# if the intersection is nonempty return the rectangle formed by their intersection

# First let's use a named tuple as a lightweight object
import collections

Rectangle = collections.namedtuple('Rectangle',['x','y','width','height'])


def intersect_rectangle(r1: Rectangle, r2: Rectangle) -> Rectangle:
    
    # Think about when rectangles don't intersect
    # Rectangles don't intersect when
    # r1.x > r2.x + r2.width
    # r1.y > r2.y + r2.height
    # r2.x > r1.x + r1.width
    # r2.y > r1.y + r1.height

    #if any of the above happens, then the 2 rectangles don't intersect
    
    conditions = [(r1.x > r2.x + r2.width), (r1.y > r2.y + r2.height), (r2.x > r1.x + r1.width),
            (r2.y > r1.y + r1.height)]
    print(conditions)
    if(any(conditions)):
        return Rectangle(0,0,-1,-1) # No intersection
    else:
        newX = max(r1.x, r2.x)
        newY = max(r1.y, r2.y)

        newWidth = (min(r1.x+r1.width, r2.x +r2.width) - newX)
        newHeight = (min(r1.y+r1.height, r2.y +r2.height) - newY)
        return Rectangle(newX, newY, newWidth, newHeight)


r1 = Rectangle(2,2, 2, 2)
r2 = Rectangle(2,2, 2, 2)

print(intersect_rectangle(r1,r2))

r1 = Rectangle(2,2, 2, 2)
r2 = Rectangle(5,4, 2, 2)

print(intersect_rectangle(r1,r2))

r1 = Rectangle(0,0, 2, 2)
r2 = Rectangle(1,0, 2, 2)

print(intersect_rectangle(r1,r2))