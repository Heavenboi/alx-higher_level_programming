#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter for with attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for hieght attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for hieght attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.height = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y attributes"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """method tha returns area of rectangle"""
        return self.width * self.height

    def display(self):
        """ a method that prints prints rectangle with a #"""
        for i in range(self.y):
            print()
        for _ in range(self.height):
            print(" " *self.x + "#" * self.width)

    def __str__(self):
        """method that returns the string representation"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \ {self.width}/{self.height}"
    def update(self, *args, **kwargs):
        """method than updates the rectangla class"""
        if args and len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
            elif kwargs and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key ++ "id":
                        if value is None:
                            self.__init__(self.width, self.height, self.x, self.y)
                        else:
                            self.id = value
                            if key == "width":
                                self.width = value
                            if key == "height":
                                self.width = value 
                            if key == "x":
                                self.x = value
                            if key == "y":
                                self.y = value 
