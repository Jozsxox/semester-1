# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):

        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        
        if name == "":
            raise ValueError("Name can't be an empty string.")

        if not isinstance(birth, date):
            raise TypeError("Birth must be a date value.")
        
        self.name = name
        self.birth = birth

    def initials(self):
        return "".join(word[0].upper() for word in self.name.split())

    def is_birthday(self):
        today = date.today()
        if today.month == self.birth.month and today.day == self.birth.day:
            return True
        else:
            return False
    


        


    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
