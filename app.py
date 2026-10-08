from models.restaurant import Restaurant
from models.assessment import Assessment
from models.menu.drink import Drink
from models.menu.plate import Plate

restaurant1 = Restaurant('Lecco Burguer', 'Burger Place', 'Active')
Restaurant.restaurants.append(restaurant1)
asses1 = Assessment('Eduardo', 10)
restaurant1.assessment.append(asses1)
drink1 = Drink('Coca Cola', 6.00, '350ml', 'Coca Cola of 350ml')
plate1 = Plate('Executive Plate', 22.00, 'Rice, beans, meet, salad and fried egg')
restaurant1.menuItems.append(drink1)
restaurant1.menuItems.append(plate1)


def main():
    Restaurant.menu()
    
if __name__ == '__main__':
    main()