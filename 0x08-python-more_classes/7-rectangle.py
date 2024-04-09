#!/usr/bin/python3
"""
class Rectangle based on 1-rectangle.py (Task 1)
"""


class Rectangle:
    """class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """class constructor"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """deleting the rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Getter: width -->  return the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter: width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter: height --> retun the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter : width"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculating the area: height * width"""
        return self.__width * self.__height

    def perimeter(self):
        """calculating the parameter -->  2 * height + 2 * width"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """string representation of rectangle"""
        strn = ""
        for j in range(self.__height):
            for j in range(self.__width):
                strn += str(self.print_symbol)
            if j != self.__height - 1:
                strn += '\n'
        return strn

    def __repr__(self):
        """string representation of the rectangle --> repr"""
        wd = str(self.__width)
        ht = str(self.__height)
        strn = "Rectangle(" + wd + ", "+ h + ")"
        return strn
