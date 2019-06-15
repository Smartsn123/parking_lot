import sys, os
import unittest
sys.path.append("{}/src/models".format(os.getcwd()))
from car import Car
from lot import Lot
from parking_lot import ParkingLot


class TestCar(unittest.TestCase):

    def testCarInit(self):
        car_reg_no = 'KA-01-BB-0001'
        car_color = 'White'
        new_car = Car(car_reg_no, car_color)
        self.assertEqual(new_car.reg_no, car_reg_no, "Car reg set test failed")
        self.assertEqual(new_car.color, car_color, "Car reg set test failed")


class TestLot(unittest.TestCase):

    def testLotInit(self):
        lot_id = 1
        lot_distance = 5
        new_lot = Lot(lot_id, lot_distance)
        self.assertEqual(new_lot.id, lot_id, "test lot constructor failed wrong assigned value")
        self.assertEqual(new_lot.distance, lot_distance, "test lot constructor failed wrong assigned value")
        self.assertEqual(new_lot.available, True, "test lot constructor failed wrong assigned value")
        self.assertEqual(new_lot.parked_car, None, "test lot constructor failed wrong assigned value")

    def testLotPark(self):
        lot_id = 1
        lot_distance = 5
        new_lot = Lot(lot_id, lot_distance)
        car_reg_no = 'KA-01-BB-0001'
        car_color = 'White'
        new_lot.park(Car(car_reg_no, car_color))
        self.assertEqual(new_lot.available, False, "lot parking function test failed")
        self.assertEqual(new_lot.parked_car.reg_no, car_reg_no, "lot parking function test failed")
        self.assertEqual(new_lot.parked_car.color, car_color, "lot parking function test failed")
        with self.assertRaises(Exception) as context:
            new_lot.park(Car(car_reg_no+'-1', car_color))
        self.assertTrue('Lot already occupied !' in str(context.exception))

    def testLotEmpty(self):
        lot_id = 1
        lot_distance = 5
        new_lot = Lot(lot_id, lot_distance)
        car_reg_no = 'KA-01-BB-0001'
        car_color = 'White'
        new_lot.park(Car(car_reg_no, car_color))
        new_lot.empty()
        self.assertEqual(new_lot.available, True, "lot empty function test failed")
        self.assertEqual(new_lot.parked_car, None, "lot empty function test failed")
        with self.assertRaises(Exception) as context:
            new_lot.empty()
        self.assertTrue('Lot already empty !' in str(context.exception))


class TestParkingLot(unittest.TestCase):

    def testInit(self):
        lots = 6
        my_parking = ParkingLot(lots)
        self.assertEqual(len(my_parking.lots.keys()), lots, "ParkingLot Constructor test failed")
        self.assertEqual(len(my_parking.available_lots), lots, "ParkingLot Constructor test failed")

    def testpark_in_lot(self):
        lots = 6
        my_parking = ParkingLot(lots)
        lot_id = my_parking.get_min_distance_lot()
        self.assertEqual(lot_id, 1, "testpark_in_lot Failed ")
        my_parking.park_in_lot(lot_id, Car('KA-01-BB-0001', 'White'))
        self.assertEqual(my_parking.lots[lot_id].available, False, "testpark_in_lot Failed")
        self.assertEqual(my_parking.lots[lot_id].parked_car.reg_no, 'KA-01-BB-0001',  "testpark_in_lot Failed")
        with self.assertRaises(Exception) as context:
            my_parking.park_in_lot(lot_id, Car('KA-01-BB-0002', 'Black'))
        self.assertTrue('Lot already occupied !' in str(context.exception))

    def testEmptyLot(self):
        lots = 6
        my_parking = ParkingLot(lots)
        lot_id1 = my_parking.get_min_distance_lot()
        my_parking.park_in_lot(lot_id1, Car('KA-01-BB-0001', 'White'))
        lot_id2 = my_parking.get_min_distance_lot()
        my_parking.park_in_lot(lot_id2, Car('KA-01-BB-0002', 'Black'))
        emptied_car = my_parking.empty_lot(lot_id1)
        self.assertEqual(emptied_car.reg_no, 'KA-01-BB-0001', "testEmptyLot Failed")
        self.assertEqual(emptied_car.color, 'White', "testEmptyLot Failed")
        self.assertEqual(my_parking.lots[lot_id1].available, True, "testEmptyLot Failed")
        self.assertEqual(my_parking.lots[lot_id1].parked_car, None, "testEmptyLot Failed")
        lot_id3 = my_parking.get_min_distance_lot()
        self.assertEqual(lot_id1, lot_id3, "testEmptyLot Failed")

    def testMinDistanceLot(self):
        lots = 9
        my_parking = ParkingLot(lots)
        lot_id1 = my_parking.get_min_distance_lot()
        self.assertEqual(lot_id1, 1, "testMinDistanceLot Failed ")
        my_parking.park_in_lot(lot_id1, Car('KA-01-BB-0001', 'White'))
        lot_id2 = my_parking.get_min_distance_lot()
        self.assertEqual(lot_id2, 2, "testMinDistanceLot Failed ")
        my_parking.park_in_lot(lot_id2, Car('KA-01-BB-0002', 'Black'))
        lot_id3 = my_parking.get_min_distance_lot()
        self.assertEqual(lot_id3, 3, "testMinDistanceLot Failed ")
        my_parking.park_in_lot(lot_id3, Car('KA-01-BB-0003', 'Blue'))
        emptied_car = my_parking.empty_lot(lot_id2)
        self.assertEqual(emptied_car.reg_no, 'KA-01-BB-0002', "testMinDistanceLot Failed")
        self.assertEqual(emptied_car.color, 'Black', "testMinDistanceLot Failed")
        lot_id4 = my_parking.get_min_distance_lot()
        self.assertEqual(lot_id2, lot_id4, "testMinDistanceLot Failed")


if __name__ == '__main__':
    unittest.main()
