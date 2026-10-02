import os, time

class Restaurant:
    
    id_counter = 0
    restaurants = []
    
    def __init__(self, name, category, status):
        self.id = Restaurant.id_counter
        self.name = name
        self.category = category
        self.status = status
        
        Restaurant.id_counter += 1
    
    # @classmethod
    # def updateName(cls):
        
    

    @staticmethod
    def updateMenu():
        option = 0
        
        print('\nUpdate Restaurant\n\nChoose one option bellow:\n\n')
        print('1. Name\n2. Category\n3. Status\n4. Exit')
        
        try:
            option = int(input('\nYour choice: '))
            time.sleep(1)
            os.system('cls')
            
            if option == 1:
                updateName()
            elif option == 2:
                updateCategory()
            elif option == 3:
                updateStatus()
            elif option == 4:
                Restaurant.menu()
            else:
                print('\nError: Invalid option!\n')
                time.sleep(2)
            
        except ValueError:
            print('\nError: Invalid input!\n')
            time.sleep(2)
            
        
    @staticmethod
    def addRestaurant():
        print('\nAdd Restaurant\n\n')
        
        name = input('Name: ')
        category = input('Category: ')
        status = 'Active'
        
        if not name or not category:
            print('\nError: Invalid value! (Empty)\n')
            time.sleep(1.5)
            Restaurant.menu()
    
        newRestaurant = Restaurant(name, category, status)
    
        Restaurant.restaurants.append(newRestaurant)
        print('\nRestaurant Added!\n')
        
        time.sleep(1.5)
        os.system('cls')
        
        
    @classmethod
    def delRestaurant(cls):
        print('\nRemove Restaurant\n\n')
        
        try:
            if not cls.restaurants:
                print('No restaurants registered!')
                time.sleep(3)
                Restaurant.menu()
                
            search_id = int(input('Inform the ID to be removed: '))
            
            for restaurant in cls.restaurants:
                if restaurant.id == search_id:
                    cls.restaurants.remove(restaurant)
                    print('\nRestaurant Removed!\n')
                    time.sleep(1.5)
                else:
                    print('\nRestaurant not found!\n')
                    time.sleep(1.5)
        
        except ValueError:
            print('\nError: Invalid value!\n')  
        
    @classmethod
    def listRestaurants(cls):
        print('\nRestaurants: ')
        
        if not cls.restaurants:
            print('\nNo restaurants registered!\n')
        
        for restaurant in cls.restaurants:
            print(f'\n{'ID'.ljust(5)} | {'Restaurant Name'.ljust(25)} | {'Category'.ljust(25)} | {'Status'.ljust(25)}')
            print(restaurant)
        
        time.sleep(3)
        os.system('cls')
            
    def __repr__(self):
            return f'{str(self.id).ljust(5)} | {self.name.ljust(25)} | {self.category.ljust(25)} | {self.activeStatus.ljust(25)}'
        
    @property
    def activeStatus(self):
        if self.status == 'Active':
            return '✅'
        else:
            return '❌'
        
    @staticmethod
    def menu ():
        
        option = 0
    
        while option != 5:
            try:
                os.system('cls')
                print('\n1. Add Restaurant\n2. Remove Restaurant\n3. List Restaurants\n4. Update Restaurant\n5. Exit')
                option = int(input('\nChoose one option: '))
                os.system('cls')

                if option == 1:
                    Restaurant.addRestaurant()
                elif option == 2:
                    Restaurant.delRestaurant()
                elif option == 3:
                    Restaurant.listRestaurants()
                elif option == 4:
                    Restaurant.updateMenu()
                else:
                    print('\nError: Invalid option!\n')
                    time.sleep(2)
                
                
            except ValueError:
                print('\nError: Invalid input!\n')
                time.sleep(2)
                
        
    