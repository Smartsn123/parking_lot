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
        self.assertEqual(new_lot.id , lot_id, "test lot constructor failed wrong assigned value")
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
        self.assertEqual(new_lot.available, True, "lot parking function test failed")
        self.assertEqual(new_lot.parked_car, None, "lot parking function test failed")
        with self.assertRaises(Exception) as context:
            new_lot.empty()
        self.assertTrue('Lot already empty !' in str(context.exception))








if __name__ == '__main__':
    unittest.main()
