
class Lot:
    """
    Class to represent a parking lot object
    All methods havae complexity of O(1)
    """

    def __init__(self, id, distance, available=True, parked_car=None):
        """
        constructor function for the Lot object
        :param id: unique id of the Lot
        :param distance: distance from the gate
        :param available: if the lot is available or not available by default
        :param parked_car: if available then Car object
        :return: return self.object by default
        Complexity : O(1)
        """
        self._id = id
        self._distance = distance
        self._available = available
        self._parked_car = parked_car

    @property
    def id(self):
        """
        getter function for id property
        :return: id property of Lot
        Complexity : O(1)
        """
        return self._id

    @property
    def distance(self):
        """
        getter function for distance property
        :return: distance property of Lot
        Complexity : O(1)
        """
        return self._distance

    @property
    def parked_car(self):
        """
        getter function for parked_car property
        :return: Car object parked at the Lot
        Complexity : O(1)
        """
        return self._parked_car

    @parked_car.setter
    def parked_car(self, value):
        """
        setter function for parked_car property
        :param value: car object that is parked
        :return: None
        Complexity : O(1)
        """
        self._parked_car = value

    @property
    def available(self):
        """
        getter function for available property
        :return: if the slot is available
        Complexity : O(1)
        """
        return self._available

    @available.setter
    def available(self, value):
        """
        setter function for available property
        :param value: available value
        :return: None
        Complexity : O(1)
        """
        self._available = value

    def empty(self):
        """
        function definition to empty the Lot
        :return: remove car from the Lot
        Complexity : O(1)
        """
        if self.available:
            raise Exception("Lot already empty !")
        self.available = True
        car_emptied = self.parked_car
        self.parked_car = None
        return car_emptied

    def park(self, car):
        """
        function definition to park car in the Lot
        :param car: car object for car that is parked
        :return: None
        Complexity : O(1)
        """
        if not self.available:
            raise Exception("Lot already occupied !")
        self.available = False
        self.parked_car = car








