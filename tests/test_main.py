import sys, os
import unittest
sys.path.append("{}/src".format(os.getcwd()))
sys.path.append("{}/tests".format(os.getcwd()))
sys.path.append("{}/src/lib".format(os.getcwd()))
from main import AppMain, ParkingLotApp
from test_libs import TestHeap
from test_models import TestCar, TestLot, TestParkingLot
from  CONSTANTS import Commands, Results


class TestParkingLotApp(unittest.TestCase):

    def setUp(self):
        self.parking_app = ParkingLotApp(9)
        self.cars =[['KA-01-HH-1234' ,'White'],
                    ['KA-01-HH-9999', 'White'],
                    ['KA-01-BB-0001', 'Black'],
                    ['KA-01-HH-7777', 'Red']]

    def tearDown(self):
        self.parking_app = None
        self.cars = None

    def reset_parking_lot(self):
        self.tearDown()
        self.setUp()
        for car in self.cars:
         self.parking_app.park_car(*car)

    def test_constructor(self):
        function_name = "ParkingLotApp.Constructor"
        print ("Running unittest cases for {}\n".format(function_name))
        self.assertListEqual(list(self.parking_app.parking_lot.lots.keys()), [i for i in range(1,10)], "unittest for {} failed ".format(function_name))

    def test_park_car(self):
        function_name = "ParkingLotApp.park_car"
        print("Running unittest cases for {}\n".format(function_name))
        self.reset_parking_lot()
        self.assertTrue(self.cars[0][0] in self.parking_app.parking_lot.cars_parked, "unittest for {} failed ".format(function_name))
        self.assertTrue(self.cars[1][0] in self.parking_app.parking_lot.cars_parked, "unittest for {} failed ".format(function_name))
        self.assertTrue(self.cars[2][0] in self.parking_app.parking_lot.cars_parked, "unittest for {} failed ".format(function_name))
        self.assertTrue(self.cars[3][0] in self.parking_app.parking_lot.cars_parked, "unittest for {} failed ".format(function_name))
        result = self.parking_app.park_car(*self.cars[2])
        self.assertEqual(result, Results.Car_present_error ,"unittest for {} failed ".format(function_name))

    def test_leave(self):
        self.reset_parking_lot()
        function_name = "ParkingLotApp.leave"
        print("Running unittest cases for {}\n".format(function_name))
        result = self.parking_app.leave(2)
        self.assertEqual(result, Results.Free_slot_success.format(2), "unittest for {} failed ".format(function_name))
        result = self.parking_app.leave(2)
        self.assertEqual(result, Results.Free_slot_failure.format(2), "unittest for {} failed ".format(function_name))

    def test_status(self):
        self.reset_parking_lot()
        function_name = "ParkingLotApp.status"
        print("Running unittest cases for {}\n".format(function_name))
        result = self.parking_app.status()
        self.assertEqual(len(result.split('\n')), 6, "unittest for {} failed ".format(function_name))
        self.parking_app.leave(1)
        result = self.parking_app.status()
        self.assertEqual(len(result.split('\n')), 5, "unittest for {} failed ".format(function_name))

    def test_filter_cars_with_colour(self):
        self.reset_parking_lot()
        function_name = "ParkingLotApp.filter_cars_with_colour"
        print("Running unittest cases for {}\n".format(function_name))
        result = self.parking_app.filter_cars_with_colour("White")
        self.assertEqual(len(result.split(',')), 2, "unittest for {} failed ".format(function_name))
        self.assertEqual(result, "KA-01-HH-1234, KA-01-HH-9999".format(function_name))
        result = self.parking_app.filter_cars_with_colour("Black")
        self.assertEqual(len(result.split(',')), 1, "unittest for {} failed ".format(function_name))
        self.assertEqual(result, "KA-01-BB-0001".format(function_name))
        result = self.parking_app.filter_cars_with_colour("White", "slot_id")
        self.assertEqual(len(result.split(',')), 2, "unittest for {} failed ".format(function_name))
        self.assertEqual(result, "1, 2".format(function_name))
        result = self.parking_app.filter_cars_with_colour("Black", "slot_id")
        self.assertEqual(len(result.split(',')), 1, "unittest for {} failed ".format(function_name))
        self.assertEqual(result, "3".format(function_name))

    def test_slot_number_for_registration_number(self):
        self.reset_parking_lot()
        function_name = "ParkingLotApp.slot_number_for_registration_number"
        print("Running unittest cases for {}\n".format(function_name))
        slot_no = self.parking_app.slot_number_for_registration_number("KA-01-HH-1234")
        self.assertEqual(slot_no, "1", "unittest for {} failed ".format(function_name))
        slot_no = self.parking_app.slot_number_for_registration_number("KA-01-BB-0001")
        self.assertEqual(slot_no, "3", "unittest for {} failed ".format(function_name))
        result = self.parking_app.slot_number_for_registration_number("KA-01-BB-0011")
        self.assertEqual(result, Results.Not_found, "unittest for {} failed ".format(function_name))



class TestAppMain(unittest.TestCase):

    def setUp(self):
        self.app = AppMain()
        self.commands = [
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
        self.results = [
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

    def tearDown(self):
        self.app = None
        self.commands = None
        self.results = None

    def test_main(self):
        print("Running all AppMain unittest cases for {}\n")
        for ix, command in enumerate(self.commands):
            result = self.app.execute(command)
            self.assertEqual(result, self.results[ix], " unit test for AppMain Failed")


if __name__ == "__main__":
    print "Running Automated test cases for the App"
    unittest.main()