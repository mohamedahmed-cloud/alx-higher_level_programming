#!/usr/bin/python3
"""
Rectangle - that inherits from Base:
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle - class that inherit from Base.
    """

    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # width property
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    # height property
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    # x property
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    # y property
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        area - return the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        display - display the rectangle using # character.
        """
        res = "\n" * self.y
        res += ((" " * self.x + "#" * self.width) + "\n") * self.height
        print(res, end="")

    def __str__(self, value="Rectangle"):
        if value == "Rectangle":
            return f"[{value}] ({self.id}) {self.x}/\
{self.y} - {self.width}/{self.height}"
        else:
            return f"[{value}] ({self.id}) {self.x}/\
{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        update - this function is used to update the attribute of the object
        """

        list = [self.id, self.width, self.height, self.x, self.y]
        dict = {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
        cnt = 0

        if args:
            for i in args:
                list[cnt] = i
                cnt += 1
        else:
            for k, v in kwargs.items():
                dict[k] = v

        [id, width, height, x, y] = list
        if not args:
            [id, width, height, x, y] = [dict["id"], dict["width"],
                                         dict["height"], dict["x"], dict["y"]]

        self.id = id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self, value="Rectangle"):
        """
        to_dictionary - provide a dictionary representation for the object.
        """
        if value == "Rectangle":
            return {"id": self.id, "width": self.width,
                    "height": self.height, "x": self.x, "y": self.y}
        else:
            return {"id": self.id, "size":
                    self.width, "x": self.x, "y": self.y}
