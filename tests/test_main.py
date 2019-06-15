import sys, os
import unittest
sys.path.append("{}/src".format(os.getcwd()))
sys.path.append("{}/tests".format(os.getcwd()))
from main import AppMain
from test_libs import TestHeap
from test_models import TestCar, TestLot, TestParkingLot


class TestCar(unittest.TestCase):

    def testMain(self):
        app = AppMain()
        commands = [
            "create_parking_lot 6\n",
            "park KA-01-HH-1234 White\n",
            "park KA-01-HH-9999 White\n",
            "park KA-01-BB-0001 Black\n",
            "park KA-01-HH-7777 Red\n",
            "park KA-01-HH-2701 Blue\n",
            "park KA-01-HH-3141 Black\n",
            "leave 4\n",
            "status\n",
            "park KA-01-P-333 White\n",
            "park DL-12-AA-9999 White\n",
            "registration_numbers_for_cars_with_colour White\n",
            "slot_numbers_for_cars_with_colour White\n",
            "slot_number_for_registration_number KA-01-HH-3141\n",
            "slot_number_for_registration_number MH-04-AY-1111\n"
        ]
        results = [
            "Created a parking lot with 6 slots\n",
            "Allocated slot number: 1\n",
            "Allocated slot number: 2\n",
            "Allocated slot number: 3\n",
            "Allocated slot number: 4\n",
            "Allocated slot number: 5\n",
            "Allocated slot number: 6\n",
            "Slot number 4 is free\n",
            "Slot No.    Registration No    Colour\n1           KA-01-HH-1234      White\n2           KA-01-HH-9999      White\n3           KA-01-BB-0001      Black\n5           KA-01-HH-2701      Blue\n6           KA-01-HH-3141      Black\n",
            "Allocated slot number: 4\n",
            "Sorry, parking lot is full\n",
            "KA-01-HH-1234, KA-01-HH-9999, KA-01-P-333\n",
            "1, 2, 4\n",
            "6\n",
            "Not found\n"
        ]
        for ix, command in enumerate(commands):
            result = app.execute(command)
            self.assertEqual(result, results[ix])


if __name__ == "__main__":
    unittest.main()