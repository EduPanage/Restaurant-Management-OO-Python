import os, time

class Assessment:
    
    def __init__(self, client, grade):
        self.client = client
        self.grade = grade
        
    def __repr__(self):
        return f'\nClient: {self.client} - Grade: {self.grade}'
    
    