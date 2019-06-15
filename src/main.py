#!/usr/bin/env python
import sys, os
sys.path.append("{}/src/models".format(os.getcwd()))
from car import Car
from parking_lot import ParkingLot

class ParkingLotApp:

    def __init__(self, slots):
        self.parking_lot = ParkingLot(slots)

    def park_car(self, reg_no, color):
        if reg_no in self.parking_lot.cars_parked:
            return "Duplicate car no , car already parked!"
        if self.parking_lot.is_slot_available():
            slot_id = self.parking_lot.get_min_distance_lot()
            self.parking_lot.park_in_lot(slot_id, Car(reg_no, color))
            return "Allocated slot number: {}".format(slot_id)
        else:
            return "Sorry, parking lot is full"

    def leave(self, slot_id):
        if not slot_id in self.parking_lot.lots:
            return "Invalid slot number"
        slot = self.parking_lot.get_slot(slot_id)
        if slot.parked_car:
            car = self.parking_lot.empty_lot(slot_id)
            return "Slot number {} is free".format(slot_id)
        else:
            return "Slot number {} is already empty".format(slot_id)


    def status(self):
        return_string = "Slot No.    Registration No    Colour\n"
        for slot in self.parking_lot.lots:
            if not self.parking_lot.lots[slot].available:
                slot_obj = self.parking_lot.get_slot(slot)
                return_string += ("{}".format(slot) + " ".join(["" for i in range(13-len(str(slot)))]) )
                return_string += "{}      ".format(slot_obj.parked_car.reg_no)
                return_string += "{}\n".format(slot_obj.parked_car.color)
        #print return_string
        return return_string

    def filter_cars_with_colour(self, color, return_property="reg_no"):
        info_list = []
        for slot_id in self.parking_lot.lots:
            if self.parking_lot.lots[slot_id].parked_car:
                car = self.parking_lot.lots[slot_id].parked_car
                if car.color.lower() == color.lower():
                    if return_property == "slot_id":
                        info_list.append(str(slot_id) )
                    else:
                        info_list.append(car.reg_no)
        return ", ".join(info_list)

    def slot_number_for_registration_number(self, reg_no):
        if reg_no in self.parking_lot.cars_parked:
            return self.parking_lot.cars_parked[reg_no]
        else:
            return "Not found"



class AppMain:

    def __init__(self):
        self.parking_lot = None

    def execute(self, command):
        if ("create_parking_lot" not in command) and self.parking_lot == None:
            return "Create the parking lot first\n"
        elif "create_parking_lot" in command :
            try:
                num = int(command.split()[1].strip())
                self.parking_lot = ParkingLotApp(num)
                return "Created a parking lot with {} slots\n".format(num)
            except Exception as e:
                return "Invalid input\n"
        elif "park" in command:
            try:
                #print("park")
                reg_no, color = [ val.strip() for val in command.split()[1:]]
                return self.parking_lot.park_car(reg_no, color)+"\n"
            except Exception as e:
                #print e
                return "Invalid input\n"

        elif "leave" in command:
            try:
                #print("leave")
                slot_no = int(command.split()[1].strip())
                return self.parking_lot.leave(slot_no)+"\n"
            except:
                return "Invalid input\n"

        elif "status" in command:
            #print("status")
            return self.parking_lot.status()

        elif "registration_numbers_for_cars_with_colour" in command:
            #print("registration")
            if len (command.split()) == 2:
                color = command.split()[1].strip().title()
                return self.parking_lot.filter_cars_with_colour(color, "reg_no")+"\n"
            else:
                return "Invalid input\n"

        elif "slot_numbers_for_cars_with_colour" in command:
            #print("case slot no color")
            if len (command.split()) == 2:
                color = command.split()[1].strip().title()
                return self.parking_lot.filter_cars_with_colour(color, "slot_id")+"\n"
            else:
                return "Invalid input\n"

        elif "slot_number_for_registration_number" in command:
            #print("case slot no reg no")
            if len (command.split()) == 2:
                reg_no = command.split()[1].strip()
                return str(self.parking_lot.slot_number_for_registration_number(reg_no))+"\n"
            else:
                return "Invalid input"
        else:
            return "Invalid input"


if __name__ == "__main__":
    app = AppMain()
    if len(sys.argv)>1:
        input_file = sys.argv[1]
        commands = open(input_file,'r').read().split('\n')
        ix = 0
        while True:
            if ix == len(commands) or commands[ix] == "exit":
                break
            else:
                sys.stdout.write(app.execute(commands[ix]))
                ix+=1
    else:
        while True:
            command = raw_input()
            if command == "exit":
                break
            else:
                sys.stdout.write(app.execute(command))



















