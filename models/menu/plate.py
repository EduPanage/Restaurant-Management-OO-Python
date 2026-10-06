from models.menu.menu_item import MenuItem

class Plate(MenuItem):
    
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self._description = description
        
        
    def __repr__ (self):
        return f'\nName: {self._name} - Price: R$ {self._price}\nDescription: {self._description}'