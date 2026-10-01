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
            print(restaurant)
        
        time.sleep(3)
        os.system('cls')
            
    def __repr__(self):
            return f'\nID: {self.id}\nName: {self.name}\nCategory: {self.category}       Status: {self.activeStatus} \n'
        
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

                if option == 1:
                    os.system('cls')
                    Restaurant.addRestaurant()
                elif option == 2:
                    os.system('cls')
                    Restaurant.delRestaurant()
                elif option == 3:
                    os.system('cls')
                    Restaurant.listRestaurants()
                
            except ValueError:
                print('\nError: Invalid option!\n')
                
        
    