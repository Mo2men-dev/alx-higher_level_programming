#!/usr/bin/python3
"""
Module that contains class Rectangle,
inheritance of class Base
"""


from base import Base


class Rectangle(Base):
    """ Rectangle Class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Init instances """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super.__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return the are of the rectangle """
        return self.width * self.height

    def display(self):
        "display the rectangle"
        rect = "\n" * self.y
        for i in range(self.height):
            rect += " " * self.x
            rect += "#" * self.width + "\n"

        print(rect)

    def __str__(self):
        """ str special method """
        str_rectangle = "[Rectangle] "
        str_id = "({:d}) ".format(self.id)
        str_x_y = "{:d}/{:d} - ".format(self.x, self.y)
        str_w_h = "{:d}/{:d}".format(self.width, self.height)

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) != 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dict of the class attrs """
        attr_list = ["id", "width", "height", "x", "y"]
        dic = {}
        for i in attr_list:
            dic[i] = getattr(self, i)

        return dic
