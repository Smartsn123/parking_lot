import sys, os
sys.path.append("{}/src/lib".format(os.getcwd()))
sys.path.append("{}/src/models".format(os.getcwd()))
from lot import Lot
from utils import CustomHeap


class ParkingLot:
    """
    Class that represents the complete parking_lot
    """

    def __init__(self, lot_count):
        """
        -constructor class for parking lot object
        -Lots are kept with ids in hashmap so that updation (empty and park operations) are fast
        :param lot_count:  count of Lot's to be in parking lot
        :return: None
        Complexity : O(n)
        """
        self.lot_count = lot_count
        self.lots = {i: Lot(i, i) for i in range(1, lot_count+1)}
        self.available_lots = CustomHeap([item for k, item in self.lots.items()],
                                         'id',
                                         'distance')

    def get_min_distance_lot(self):
        """
        :return: Get parking lot id for the Minimum distance empty lot
        Complexity : O(log-n)
        """
        if len(self.available_lots) == 0:
            raise Exception("Sorry, parking lot is full")
        minim_distance, nearest_lot_id = self.available_lots.extract_min()
        return nearest_lot_id

    def empty_lot(self, lot_id):
        """
        -function to empty the parking Lot with given id
        :param lot_id: id of the lot that is to be marked filled
        :return: None
        Complexity : O(log-n)
        """
        self.available_lots.insert(self.lots[lot_id])
        car = self.lots[lot_id].empty()
        return car

    def park_in_lot(self, lot_id, car):
        """
        function to park car in lot with given Lot id
        :param lot_id:  id of the lot that is to be marked empty
        :return: None
        Complexity : O(1)
        """
        self.lots[lot_id].park(car)
