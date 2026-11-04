# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.

        Parameters:
            width (int): The width of the rectangle, must be positive.
            height (int): The height of the rectangle, must be positive.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to zero.
        """

        if not isinstance(width, int):
            raise TypeError("Width must be an integer.")

        if width <= 0:
            raise ValueError("Width must be greater than 0.")

        if not isinstance(height, int):
            raise TypeError("Height must be an integer.")

        if height <= 0:
            raise ValueError("Height must be greater than 0.")

        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height

    def is_square(self):
        """
        Return True if this rectangle is a square, otherwise False.
        """
        return self.width == self.height

    def area(self):
        """
        Return the area of the rectangle.
        """
        return self.width*self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.
        """
        return 2*(self.width+self.height)


    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
