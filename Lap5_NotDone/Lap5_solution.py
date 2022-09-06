
# Exercise 2
import logging
from Apartment import Apartment
logging.basicConfig(filename='apartmentLog.log', filemode='a', format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', level=logging.DEBUG)

ap1 = Apartment(3, False, False, 1000)
ap2 = Apartment(5, True, True, 2000)
ap3 = Apartment(3, True, False, 1200)
ap4 = Apartment(2, False, True, 800)
ap5 = Apartment(4, True, False, 1700)
ap6 = Apartment(3, False, False, 1000)
ap7 = Apartment(4, False, True, 1500)

print(ap1)
print(ap2)
print(ap3)
print(ap4)
print(ap5)
print(ap6)
print(ap7)


# Exercise 3

listOfAppartment = []
listOfAppartment.append(ap1)
listOfAppartment.append(ap2)
listOfAppartment.append(ap3)
listOfAppartment.append(ap4)
listOfAppartment.append(ap5)
listOfAppartment.append(ap6)
listOfAppartment.append(ap7)

# Exercise 4

def num_Avaliable(self, list):
    count = 0
    for i in list:
       if isinstance(i, self) and i.Rented == False:
           count +=1
       else:
            logging.error("Apartment already rented")

    return count

print(num_Avaliable(Apartment,listOfAppartment))


def num_Apartment_Rooms(self, list, rNum):
    logging.warning("Searching for Apartment room")
    count = 0
    for i in list:
       if isinstance(i, self) and i.RoomsNum == rNum:
           count +=1
    return count

print(num_Apartment_Rooms(Apartment,listOfAppartment, 4))

def apartment_Search(self, list, park, price):
    logging.info("Searching for specfic apartment")
    for i in list:
       if isinstance(i, self) and i.Parking == park and i.Price < price:
           print(i)

apartment_Search(Apartment, listOfAppartment, True, 1400)

# Exercise 5
# In The code