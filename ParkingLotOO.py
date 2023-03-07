"""
Problem specification:

Design a parking lot using object-oriented principles
  Here are a few methods that you should be able to run:
    Tell us how many spots are remaining
    Tell us how many total spots are in the parking lot
    Tell us when the parking lot is full
    Tell us when the parking lot is empty
    Tell us when certain spots are full e.g. when all motorcycle spots are taken
    Tell us how many spots vans are taking up

Assumptions:
    The parking lot can hold motorcycles, cars and vans
    The parking lot has motorcycle spots, car spots and large spots
    A motorcycle can park in any spot
    A car can park in a single compact spot, or a regular spot
    A van can park, but it will take up 3 regular spots
    These are just a few assumptions. Feel free to ask your interviewer about more assumptions as needed

Solution specification:
Firstly, we need to identify the different classes that we will need to create for this system. Based on the
requirements, we can start with the following classes:

1. ParkingLot
2. ParkingSpot
3. MotorcycleSpot (subclass of ParkingSpot)
4. CarSpot (subclass of ParkingSpot)
5. VanSpot (subclass of ParkingSpot)
6. Vehicle

The ParkingLot class will have information about the total number of spots, how many spots are currently occupied,
and how many spots are vacant. It will also have methods to add a vehicle, remove a vehicle, and check if the parking
lot is full or empty.
The ParkingSpot class will be an abstract class that defines the basic properties of a parking spot, such as its size
and location. The MotorcycleSpot, CarSpot, and VanSpot classes will inherit from the ParkingSpot class and provide
additional information specific to those types of spots, such as their size and capacity.

The Vehicle class will represent a vehicle that can be parked in the parking lot. It will have properties such as the
type of vehicle, license plate number, and the size of the vehicle.

"""


class ParkingSpot:
    def __init__(self, size):
        self.size = size
        self.vehicle = None

    def is_empty(self):
        return self.vehicle is None

    def park(self, vehicle):
        if self.is_empty():
            self.vehicle = vehicle
            return True
        return False

    def remove_vehicle(self):
        self.vehicle = None


class MotorcycleSpot(ParkingSpot):
    def __init__(self):
        super().__init__(size='motorcycle')


class CarSpot(ParkingSpot):
    def __init__(self, size):
        super().__init__(size)


class VanSpot(ParkingSpot):
    def __init__(self):
        super().__init__(size='large')


class Vehicle:
    def __init__(self, vehicle_type, license_plate, size):
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.size = size


class Motorcycle(Vehicle):
    def __init__(self, license_plate):
        super().__init__(vehicle_type='motorcycle', license_plate=license_plate, size='motorcycle')


class Car(Vehicle):
    def __init__(self, license_plate, size):
        super().__init__(vehicle_type='car', license_plate=license_plate, size=size)


class Van(Vehicle):
    def __init__(self, license_plate):
        super().__init__(vehicle_type='van', license_plate=license_plate, size='large')


class ParkingLot:
    def __init__(self, num_motorcycle_spots, num_car_spots, num_van_spots):
        self.num_motorcycle_spots = num_motorcycle_spots
        self.num_car_spots = num_car_spots
        self.num_van_spots = num_van_spots
        self.occupied_spots = {}

    def add_vehicle(self, vehicle):
        if isinstance(vehicle, Motorcycle):
            if self.num_motorcycle_spots > 0:
                self.num_motorcycle_spots -= 1
                self.occupied_spots[vehicle.license_plate] = MotorcycleSpot()
                return True
        elif isinstance(vehicle, Car):
            if self.num_car_spots > 0:
                if vehicle.size == 'compact':
                    self.num_car_spots -= 1
                    self.occupied_spots[vehicle.license_plate] = CarSpot(size='compact')
                    return True
                elif vehicle.size == 'regular':
                    if self.num_car_spots > 1:
                        self.num_car_spots -= 2
                        self.occupied_spots[vehicle.license_plate] = CarSpot(size='regular')
                        return True
        elif isinstance(vehicle, Van):
            if self.num_van_spots > 0:
                if self.num_car_spots > 2:
                    self.num_car_spots -= 3
                    self.num_van_spots -= 1
                    self.occupied_spots[vehicle.license_plate] = VanSpot()
                    return True
        return False

    def remove_vehicle(self, vehicle):
        if vehicle.license_plate in self.occupied_spots:
            spot = self.occupied_spots[vehicle.license_plate]
            if isinstance(spot, MotorcycleSpot):
                self.num_motorcycle_spots += 1
            elif isinstance(spot, CarSpot):
                if spot.size == 'compact':
                    self.num_car_spots += 1
                elif spot.size == 'regular':
                    self.num_car_spots += 2
            elif isinstance(spot, VanSpot):
                self.num_car_spots += 3
                self.num_van_spots += 1
            del self.occupied_spots[vehicle.license_plate]

    def is_full(self):
        return self.num_motorcycle_spots == 0 and self.num_car_spots == 0 and self.num_van_spots == 0


