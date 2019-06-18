

class Results(object):
    Car_present_error = "Duplicate car no , car already parked!"
    Slot_allocate_success = "Allocated slot number: {}"
    Parking_lot_full = "Sorry, parking lot is full"
    Invalid_slot = "Invalid slot number"
    Free_slot_success = "Slot number {} is free"
    Free_slot_failure = "Slot number {} is already empty"
    Not_found = "Not found"
    Create_parking_lot_error = "Create the parking lot first"
    Create_parking_lot_success = "Created a parking lot with {} slots"
    Invalid_input = "Invalid input"


class Commands(object):
    Create_parking_lot = "create_parking_lot"
    Park = "park"
    Leave = "leave"
    Status = "status"
    Registration_numbers_for_cars_with_colour = "registration_numbers_for_cars_with_colour"
    Slot_numbers_for_cars_with_colour = "slot_numbers_for_cars_with_colour"
    Slot_number_for_registration_number = "slot_number_for_registration_number"
    Exit = "exit"

