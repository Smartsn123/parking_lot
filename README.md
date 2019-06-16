# ParkingLotApp

An Automated ticketing system for parking Lot that allows customers to use my parking lot without human intervention.
When a car enters a parking lot,  ticket issued to the driver. The
ticket issuing process includes us documenting the registration number (number plate) and the colour of the car and allocating an available parking slot to the car

before actually handing over a ticket to the driver (we assume that our customers are nice enough to always park in the slots allocated to them).

The customer is 
allocated a parking slot which is nearest to the entry. At the exit the customer returns
the ticket which then marks the slot they were using as being available

## Getting Started
### Project structure


```
parking_lot/
|-- README.md
|-- bin
|   |-- parking_lot
|   |-- parking_lot.sh
|   |-- run_functional_tests
|   |-- setup
|   `-- setup.sh
|-- file_inputs.txt
|-- functional_spec
|   |-- Gemfile
|   |-- Gemfile.lock
|   |-- README.md
|   |-- Rakefile
|   |-- fixtures
|   |   `-- file_input.txt
|   `-- spec
|       |-- end_to_end_spec.rb
|       |-- parking_lot_spec.rb
|       `-- spec_helper.rb
|-- requirements.txt
|-- src
|   |-- __init__.py
|   |-- lib
|   |   `-- utils.py
|   |   
|   |-- main.py
|   `-- models
|       |-- __init__.py
|       |-- car.py
|       |-- lot.py
|       `-- parking_lot.py
`-- tests
    |-- test_libs.py
    |-- test_main.py
    `-- test_models.py
```

* src directory contains the python source files containing:
   * main.py : consolidated python execution  file
   * lib: supporting library code : utils.py : code for custom heap class
   * models : contains class definition for the Objects Car, Lot, ParkingLot

* tests directory contains unit tests for models, lib and main App, all executable from test_main.py

* bin directory has executables to setup and run the project

* functional_spec contains files to support run functional test suit


### Installing

Once u have cloned/uncompressed project in your directory say parking_lot, change to the project directory

```
$ cd parking_lot
```

run setup file

```
$ bin/setup
```

This will setup the parking_lot executable file for u in the bin directory and Run unittests

On successful installation you should see messages similiar to below :

```
Building ParkingLotApp version 1.0
Reading package lists... Done
Building dependency tree
Reading state information... Done
python is already the newest version (2.7.15~rc1-1).
python-pip is already the newest version (9.0.1-2.3~ubuntu1.18.04.1).
0 upgraded, 0 newly installed, 0 to remove and 9 not upgraded.
You must give at least one requirement to install (see "pip help install")
Running Automated test cases for the App
testCarInit (test_models.TestCar) ... ok
testInit (test_libs.TestHeap) ... ok
testInsert (test_libs.TestHeap) ... ok
testNodeMap (test_libs.TestHeap) ... ok
testRemoveNode (test_libs.TestHeap) ... ok
testextract_min (test_libs.TestHeap) ... ok
testLotEmpty (test_models.TestLot) ... ok
testLotInit (test_models.TestLot) ... ok
testLotPark (test_models.TestLot) ... ok
test_main (__main__.TestMain) ... ok
testEmptyLot (test_models.TestParkingLot) ... ok
testInit (test_models.TestParkingLot) ... ok
testMinDistanceLot (test_models.TestParkingLot) ... ok
testpark_in_lot (test_models.TestParkingLot) ... ok

----------------------------------------------------------------------
Ran 14 tests in 0.009s

OK
Setup done Successfully!
```

## Running the tests

You can test the executable file using sample input file "file_input.txt" in following manner:
```
bin/parking_lot file_inputs.txt
```

Output will be the sequence of operations results with the parking Lot

```
Created a parking lot with 6 slots
Allocated slot number: 1
Allocated slot number: 2
Allocated slot number: 3
Allocated slot number: 4
Allocated slot number: 5
Allocated slot number: 6
Slot number 4 is free
Slot No.    Registration No    Colour
1           KA-01-HH-1234      White
2           KA-01-HH-9999      White
3           KA-01-BB-0001      Black
5           KA-01-HH-2701      Blue
6           KA-01-HH-3141      Black
Allocated slot number: 4
Sorry, parking lot is full
KA-01-HH-1234, KA-01-HH-9999, KA-01-P-333
1, 2, 4
6
Not found
```


### Usage and Interactive mode

* create a parking lot with 6 cars
```
$ create_parking_lot 6
>Created a parking lot with 6 slots
```

* parking a car
```
$ park KA-01-HH-1234 White
>Allocated slot number: 1
```
```
$ park KA-01-HH-9999 White
>Allocated slot number: 2
```
```
$ park KA-01-HH-7777 Red
>Allocated slot number: 3
```
* empty the parking slot
```
> $ leave 3
Slot number 3 is free
```

* registration number of all cars of given colour
```
$ registration_numbers_for_cars_with_colour White
> KA-01-HH-1234, KA-01-HH-9999
```

* parking slot number of all cars of given colour
```
$ slot_numbers_for_cars_with_colour White
> 1, 2
```

* slot number for the given car
```
$slot_number_for_registration_number KA-01-HH-9999
> 3
```
```
$slot_number_for_registration_number KA-01-HH-9991
> Not found
```

## Code Time Complexity
Assuming there are N parking lots,  big O Complexity for various operations are given.
* create_parking_lot:  O(N) Time

* park :  O(logN) time (searches nearest empty slot from availabe slot heap)
* leave : O(longN) time (updation of availabe slots heap)
* registration_numbers_for_cars_with_colour:  O(N) time
* slot_numbers_for_cars_with_colour: O(N)
* status :   takes O(N) Time
* slot_number_for_registration_number : O(1)





## Authors

* **Sunny Singh** - [Smartsn123](https://github.com/Smartsn123)
