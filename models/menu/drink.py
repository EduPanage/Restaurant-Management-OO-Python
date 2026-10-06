from models.menu.menu_item import MenuItem

class Drink(MenuItem):
    
    def __init__(self, name, price, size, description):
        super().__init__(name, price)
        self._size = size
        self._description = description
        
    def __repr__ (self):
        return f'\nName: {self._name} (Size: {self._size}) - Price: R$ {self._price}\nDescription: {self._description}'
    
    
