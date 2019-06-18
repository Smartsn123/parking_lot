import sys, os
import unittest
sys.path.append("{}/src/models".format(os.getcwd()))
from car import Car
from lot import Lot
from parking_lot import ParkingLot


class TestCar(unittest.TestCase):

    def testCarInit(self):
        function_name = "Lot.__init__"
        car_reg_no = 'KA-01-BB-0001'
        car_color = 'White'
        new_car = Car(car_reg_no, car_color)
        self.assertEqual(new_car.reg_no, car_reg_no, "unittest for {} failed ".format(function_name))
        self.assertEqual(new_car.color, car_color, "unittest for {} failed ".format(function_name))


class TestLot(unittest.TestCase):

    def testLotInit(self):
        function_name = "Lot.__init__"
        lot_id = 1
        lot_distance = 5
        new_lot = Lot(lot_id, lot_distance)
        self.assertEqual(new_lot.id, lot_id, "unittest for {} failed ".format(function_name))
        self.assertEqual(new_lot.distance, lot_distance, "unittest for {} failed ".format(function_name))
        self.assertEqual(new_lot.available, True, "unittest for {} failed ".format(function_name))
        self.assertEqual(new_lot.parked_car, None, "unittest for {} failed ".format(function_name))

    def testLotPark(self):
        function_name = "Lot.park"
        lot_id = 1
        lot_distance = 5
        new_lot = Lot(lot_id, lot_distance)
        car_reg_no = 'KA-01-BB-0001'
        car_color = 'White'
        new_lot.park(Car(car_reg_no, car_color))
        self.assertEqual(new_lot.available, False, "unittest for {} failed ".format(function_name))
        self.assertEqual(new_lot.parked_car.reg_no, car_reg_no,  "unittest for {} failed ".format(function_name))
        self.assertEqual(new_lot.parked_car.color, car_color,  "unittest for {} failed ".format(function_name))
        with self.assertRaises(Exception) as context:
            new_lot.park(Car(car_reg_no+'-1', car_color))
        self.assertTrue('Lot already occupied !' in str(context.exception), "unittest for {} failed ".format(function_name))

    def testLotEmpty(self):
        function_name = "Lot.available"
        lot_id = 1
        lot_distance = 5
        new_lot = Lot(lot_id, lot_distance)
        car_reg_no = 'KA-01-BB-0001'
        car_color = 'White'
        new_lot.park(Car(car_reg_no, car_color))
        new_lot.empty()
        self.assertEqual(new_lot.available, True,  "unittest for {} failed ".format(function_name))
        self.assertEqual(new_lot.parked_car, None,  "unittest for {} failed ".format(function_name))
        with self.assertRaises(Exception) as context:
            new_lot.empty()
        self.assertTrue('Lot already empty !' in str(context.exception), "unittest for {} failed ".format(function_name))


class TestParkingLot(unittest.TestCase):

    def testInit(self):
        lots = 6
        my_parking = ParkingLot(lots)
        function_name = "ParkingLot.__init__"
        self.assertEqual(len(my_parking.lots.keys()), lots,  "unittest for {} failed ".format(function_name))
        self.assertEqual(len(my_parking.available_lots), lots, "unittest for {} failed ".format(function_name))

    def test_park_in_lot(self):
        lots = 6
        my_parking = ParkingLot(lots)
        lot_id = my_parking.get_min_distance_lot()
        function_name = "ParkingLot.park_in_lot"
        self.assertEqual(lot_id, 1,"unittest for {} failed ".format(function_name))
        my_parking.park_in_lot(lot_id, Car('KA-01-BB-0001', 'White'))
        self.assertEqual(my_parking.lots[lot_id].available, False, "unittest for {} failed ".format(function_name))
        self.assertEqual(my_parking.lots[lot_id].parked_car.reg_no, 'KA-01-BB-0001',  "unittest for {} failed ".format(function_name))
        with self.assertRaises(Exception) as context:
            my_parking.park_in_lot(lot_id, Car('KA-01-BB-0002', 'Black'))
        self.assertTrue('Lot already occupied !' in str(context.exception), "unittest for {} failed ".format(function_name))

    def testEmptyLot(self):
        lots = 6
        function_name = "ParkingLot.empty_lot"
        my_parking = ParkingLot(lots)
        lot_id1 = my_parking.get_min_distance_lot()
        my_parking.park_in_lot(lot_id1, Car('KA-01-BB-0001', 'White'))
        lot_id2 = my_parking.get_min_distance_lot()
        my_parking.park_in_lot(lot_id2, Car('KA-01-BB-0002', 'Black'))
        emptied_car = my_parking.empty_lot(lot_id1)
        self.assertEqual(emptied_car.reg_no, 'KA-01-BB-0001', "unittest for {} failed ".format(function_name))
        self.assertEqual(emptied_car.color, 'White', "testEmptyLot Failed")
        self.assertEqual(my_parking.lots[lot_id1].available, True, "unittest for {} failed ".format(function_name))
        self.assertEqual(my_parking.lots[lot_id1].parked_car, None, "unittest for {} failed ".format(function_name))
        lot_id3 = my_parking.get_min_distance_lot()
        self.assertEqual(lot_id1, lot_id3, "unittest for {} failed ".format(function_name))

    def testMinDistanceLot(self):
        lots = 9
        function_name = "ParkingLot.get_minimum_distance_lot"
        my_parking = ParkingLot(lots)
        lot_id1 = my_parking.get_min_distance_lot()
        self.assertEqual(lot_id1, 1, "unittest for {} failed ".format(function_name))
        my_parking.park_in_lot(lot_id1, Car('KA-01-BB-0001', 'White'))
        lot_id2 = my_parking.get_min_distance_lot()
        self.assertEqual(lot_id2, 2, "unittest for {} failed ".format(function_name))
        my_parking.park_in_lot(lot_id2, Car('KA-01-BB-0002', 'Black'))
        lot_id3 = my_parking.get_min_distance_lot()
        self.assertEqual(lot_id3, 3, "unittest for {} failed ".format(function_name))
        my_parking.park_in_lot(lot_id3, Car('KA-01-BB-0003', 'Blue'))
        emptied_car = my_parking.empty_lot(lot_id2)
        self.assertEqual(emptied_car.reg_no, 'KA-01-BB-0002', "unittest for {} failed ".format(function_name))
        self.assertEqual(emptied_car.color, 'Black', "unittest for {} failed ".format(function_name))
        lot_id4 = my_parking.get_min_distance_lot()
        self.assertEqual(lot_id2, lot_id4, "unittest for {} failed ".format(function_name))


if __name__ == '__main__':
    unittest.main()
