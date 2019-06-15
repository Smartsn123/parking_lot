
class Car:
    """
    Class to represent a car object
    """

    def __init__(self, reg_no, color):
        """
        Constructor for Car class variables
        :param reg_no: registration no of the car
        :param color: color of the car
        :return: returns car object by default
        Complexity : O(1)
        """
        self._reg_no = reg_no
        self._color = color

    @property
    def reg_no(self):
        """
        :return: property getter for car's registration no
        Complexity : O(1)
        """
        return self._reg_no

    @property
    def color(self):
        """
        :return: property getter for car's color
        Complexity : O(1)
        """
        return self._color