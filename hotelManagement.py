import random
import emoji
class hotelManagement():
    def __init__(self):
        self.id = 0
        self.name = " "
        self.phoneNumber = " "
        self.address = " "
        self.proof = " "
        self.inDate = " "
        self.outDate = " "
        self.roomNo = 0
        self.customers = {}
        self.rent = 0
        self.foodPrice = 0

    def addCustomer(self):
        self.name = input("Enter name : ")
        self.phoneNumber = input("Enter phone Number : ")
        self.address = input("Enter address : ")
        self.proof = input("Show proof : ")
        self.inDate = input("Enter the check in date : ")
        self.outDate = input("Enter the check put date : ")
        self.roomNo = random.randint(1,401)
        self.id = self.id+1
        print("Customer has been added successfully")
        data = f"Name : {self.name} \nProof submited : {self.proof}\nPhone Number : {self.phoneNumber}\nAddress = {self.address}\nCheck in date : {self.inDate}\nCheck out date : {self.outDate}\nRoom No : {self.roomNo}"
        self.customers[self.id] = data
        self.roomRent()

    def roomRent(self):
        print("1. Class A --> 10000")
        print("2. Class B --> 8000")
        print("3. Class C --> 6000")
        roomType = int(input("Enter the room type : "))
        noNights = int(input("Enter the number of nights : "))
        if(roomType == 1):
            cost = 10000
        elif(roomType == 2):
            cost = 8000
        elif(roomType == 3):
            cost = 6000
        self.rent = cost*noNights
        print("Your choosen room rent is : ",self.rent)

    def foodPurchased(self):
        print("1. Veg Thali -->500\n2. Non veg thali --> 550\n3. Breakfast --> 250\n4. Drinks --> 100\n5. Dessert-->200\n6. Exit")
        Continue = True
        while(Continue):
            option = int(input("Enter your choice : "))
            quantity = int(input("Enter quantity : "))
            if option == 1:
                cost = 500
            elif option == 2:
                cost = 550
            elif option == 3:
                cost = 250
            elif option == 4:
                cost = 100
            elif option == 5:
                cost = 200
            if option == 6:
                Continue = False
        self.foodPrice = self.foodPrice + cost*quantity
        print(f"Total food cost = {self.foodPrice}Rs\n")

    def costEstimation(self):
        if self.name != " ":
            print("*** Final Bill *** ")
            print("Customer Details")
            print("Room number : ",self.roomNo)
            print("Name : ",self.name)
            print("Phone number : ",self.phoneNumber)
            print("Address : ",self.address)
            print("Check in date : ",self.inDate)
            print("Check out date : ",self.outDate)
            print("Total room rent : ",self.rent)
            print("Total Food Cost : ",self.foodPrice)
            Total = self.rent + self.foodPrice + 100
            print("Your sub total purchase is : ",Total)
            print("Additional service tax : ")
            print("Total bill",Total + 500)
            print("Thank You..Visit Again ",emoji.emojize(":grinning_face_with_big_eyes:"))
        else:
            print("Add customer first.")

    def customerInfo(self):
        for i in self.customers:
            print(self.customers[i],"\n")

if __name__ == '__main__':
        hotel = hotelManagement()
        Continue = True
        while(Continue):
            print("1. Enter customer details")
            print("2. Calculate room rent")
            print("3. Calculate food purchased")
            print("4. Display total cost")
            print("5. Customers information")
            print("6. Exit")
            option = int(input("Enter the option : "))
            if(option == 1):
                hotel.addCustomer()
            elif(option == 2):
                hotel.roomRent()
            elif(option == 3):
                hotel.foodPurchased()
            elif(option == 4):
                hotel.costEstimation()
            elif(option == 5):
                hotel.customerInfo()
            elif(option == 6):
                Continue = False

