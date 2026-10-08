import os
import time
from models.assessment import Assessment
from models.menu.drink import Drink
from models.menu.plate import Plate

class Restaurant:

    id_counter = 0
    restaurants = []

    def __init__(self, name, category, status):
        self.id = Restaurant.id_counter
        self.name = name.title()
        self.category = category.title()
        self.status = status
        self.assessment = []
        self.menuItems = []

        Restaurant.id_counter += 1

    @classmethod
    def addItem(cls):
        print("\n--- Add Item to Restaurant Menu ---")

        if not cls.restaurants:
            print("\nNo restaurants registered!\n")
            time.sleep(2)
            return

        try:
            insertedID = int(input("\nRestaurant ID: "))

            found_restaurant = next(
                (r for r in cls.restaurants if r.id == insertedID), None
            )

            if found_restaurant:
                
                print("\nSelect item type:")
                print("1. Drink\n2. Plate")
                choice = int(input("Your choice: "))

                if choice == 1:
                    
                    newItem = input("\nInsert the drink name: ").strip()
                    itemPrice = float(input("Insert the price: R$ "))
                    drinkSize = input("Insert the size (ex: 350ml): ").strip()
                    drinkDesc = input("Insert a short description: ").strip()

                    if newItem and itemPrice > 0 and drinkSize and drinkDesc:
                        
                        item = Drink(newItem, itemPrice, drinkSize, drinkDesc)
                        found_restaurant.menuItems.append(item)

                        print(
                            f'\nSuccess! Drink "{newItem}" was saved on {found_restaurant.name}!\n'
                        )
                    else:
                        print("\nError: Invalid values inserted!\n")

                elif choice == 2:
                    newItem = input("\nInsert the plate name: ").strip()
                    itemPrice = float(input("Insert the price: R$ "))
                    plateDesc = input("Insert a short description: ").strip()

                    if newItem and itemPrice > 0 and plateDesc:

                        item = Plate(newItem, itemPrice, plateDesc)
                        found_restaurant.menuItems.append(item)

                        print(
                            f'\nSuccess! Plate "{newItem}" was saved on {found_restaurant.name}!\n'
                        )
                    else:
                        print("\nError: Invalid values inserted!\n")
                else:
                    print("\nError: Invalid option chosen!\n")
            else:
                print("\nError: Restaurant ID not found!\n")

            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")

        except ValueError:
            print("\nError: Invalid input! (Price and Option must be numbers)\n")
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
            
    @staticmethod
    def manageRestaurant():
        pass

    def averageAssess(self):
        if not self.assessment:
            return 0

        sumAll = sum(assessment.grade for assessment in self.assessment)
        quant = len(self.assessment)
        average = round(sumAll / quant)

        return average



    @classmethod
    def addAssess(cls):
        print("\n--- Add Assessment ---")

        if not cls.restaurants:
            print("\nNo restaurants registered!\n")
            time.sleep(2)
            return

        try:
            insertedID = int(input("\nRestaurant ID: "))

            found_restaurant = next(
                (r for r in cls.restaurants if r.id == insertedID), None
            )

            if found_restaurant:
                client_name = input("Your Name (Client): ").title()
                grade_input = int(input("Insert a grade from 1 to 10: "))

                if 1 <= grade_input <= 10:
                    new_assessment = Assessment(client_name, grade_input)
                    found_restaurant.assessment.append(new_assessment)

                    print(
                        f"\nSuccess! {client_name}'s assessment was saved (Grade: {grade_input})!\n"
                    )
                else:
                    print("\nError: Grade must be between 1 and 10!\n")
            else:
                print("\nError: Restaurant ID not found!\n")

            time.sleep(2)
            os.system("cls")

        except ValueError:
            print("\nError: Invalid input!\n")
            time.sleep(2)
            os.system("cls")
            
            
            

    @staticmethod
    def assessmentMenu():
        while True:
            print("\nAssessment Menu\n\nChoose one option below:\n")
            print("1. Add\n4. Exit")

            try:
                option = int(input("\nYour choice: "))
                os.system("cls" if os.name == "nt" else "clear")

                if option == 1:
                    Restaurant.addAssess()
                elif option == 4:
                    break
                else:
                    print("\nError: Invalid option!\n")
                    time.sleep(2)

            except ValueError:
                print("\nError: Invalid input!\n")
                time.sleep(2)
                
                
                

    @classmethod
    def updateName(cls):
        print("\n--- Update Name ---")

        try:
            restID = int(input("\nRestaurant ID: "))
        except ValueError:
            print("\nError: Invalid ID inserted!\n")
            time.sleep(2)
            return

        newName = input("New name: ")
        found = False

        for restaurant in cls.restaurants:
            if restaurant.id == restID:
                restaurant.name = newName.title()
                found = True
                print(f'\nSuccess: Name updated to "{restaurant.name}"!')
                time.sleep(2)
                break

        if not found:
            print("\nError: Restaurant ID not found!\n")
            time.sleep(2)
            
            
            

    @staticmethod
    def updateMenu():
        while True:
            print("\nUpdate Restaurant\n\nChoose one option below:\n")
            print("1. Name\n4. Exit")

            try:
                option = int(input("\nYour choice: "))
                os.system("cls" if os.name == "nt" else "clear")

                if option == 1:
                    Restaurant.updateName()
                elif option == 4:
                    break
                else:
                    print("\nError: Invalid option!\n")
                    time.sleep(2)

            except ValueError:
                print("\nError: Invalid input!\n")
                time.sleep(2)
                
                
                

    @staticmethod
    def addRestaurant():
        print("\n--- Add Restaurant ---\n")

        name = input("Name: ")
        category = input("Category: ")
        status = "Active"

        if not name.strip() or not category.strip():
            print("\nError: Invalid value! (Empty)\n")
            time.sleep(1.5)
            return

        newRestaurant = Restaurant(name, category, status)
        Restaurant.restaurants.append(newRestaurant)
        print("\nRestaurant Added!\n")
        time.sleep(1.5)
        
        
        

    @classmethod
    def delRestaurant(cls):
        print("\n--- Remove Restaurant ---\n")

        if not cls.restaurants:
            print("No restaurants registered!")
            time.sleep(2)
            return

        try:
            search_id = int(input("Inform the ID to be removed: "))

            found_restaurant = next(
                (r for r in cls.restaurants if r.id == search_id), None
            )

            if found_restaurant:
                cls.restaurants.remove(found_restaurant)
                print("\nRestaurant Removed!\n")
            else:
                print("\nRestaurant not found!\n")

            time.sleep(1.5)

        except ValueError:
            print("\nError: Invalid value!\n")
            time.sleep(2)
            
            
            

    @classmethod
    def listRestaurants(cls):
        print("\nRestaurants List:\n")

        if not cls.restaurants:
            print("No restaurants registered!\n")
        else:
            print(
                f"{'ID'.center(5)} | {'Restaurant Name'.center(20)} | {'Category'.center(20)} | {'Status'.center(15)} | {'Average'.center(8)}"
            )
            print("-" * 80)
            for restaurant in cls.restaurants:
                print(restaurant)

        print("\n")
        input("Press Enter to return to menu...")
        
        
    

    def __repr__(self):

        avg = self.averageAssess()
        avg_display = str(avg) if avg > 0 else "-"

        return f"{str(self.id).center(5)} | {self.name.center(20)} | {self.category.center(20)} | {self.activeStatus.center(15)} | {avg_display.center(8)}"




    @property
    def activeStatus(self):
        return "✅" if self.status == "Active" else "❌"
    
    
    

    @staticmethod
    def menu():
        option = 0
        while option != 7:
            try:
                os.system("cls" if os.name == "nt" else "clear")
                print(
                    "\n1. Add Restaurant\n2. Remove Restaurant\n3. List Restaurants\n4. Update Restaurant\n5. Assessment\n6. Manage Restaurant Menu\n7. Exit"
                )
                option = int(input("\nChoose one option: "))
                os.system("cls" if os.name == "nt" else "clear")

                if option == 1:
                    Restaurant.addRestaurant()
                elif option == 2:
                    Restaurant.delRestaurant()
                elif option == 3:
                    Restaurant.listRestaurants()
                elif option == 4:
                    Restaurant.updateMenu()
                elif option == 5:
                    Restaurant.assessmentMenu()
                elif option == 6:
                    Restaurant.addItem()
                elif option == 7:
                    print("\nExiting application... See you soon!")
                else:
                    print("\nError: Invalid option!\n")
                    time.sleep(2)

            except ValueError:
                print("\nError: Invalid input!\n")
                time.sleep(2)
