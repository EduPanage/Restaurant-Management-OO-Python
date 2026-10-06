class MenuItem:
    
    def __init__(self, name, price):
        self._name = name
        self._price = price
    
    def __repr__ (self):
        return f'\nName: {self._name} - Price: R$ {self._price}'