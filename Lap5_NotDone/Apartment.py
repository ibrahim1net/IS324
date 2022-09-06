# Exercise 1

class Apartment:
    def __init__(self,ro, pa ,re, pr):
        self.RoomsNum = ro
        self.Parking = pa
        self.Rented = re
        self.Price = pr

    def __str__(self):
        return "RoomNumber: " + str(self.RoomsNum) + ", Parking: " + str(self.Parking) + ", Rented: " + str(self.Rented) + ", Price: " + str(self.Price) + "$ ."



