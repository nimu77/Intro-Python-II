# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = Item('sword', 'deadly weapon')
        # self.n_to = n_to
        # self.s_to = s_to
        # self.e_to = e_to
        # self.w_to = w_to
        # , n_to=None, s_to=None, e_to=None, w_to=None
    def __str__(self):
        return f'{self.name}, {self.description}'

    # def 