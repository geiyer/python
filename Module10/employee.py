""" Employee class using property"""
class Employee:
    """Employee class"""
    def __init__(self, name=''):         # Constructor
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        #validate if the value and then set the property
        if value.isdigit():
            raise ValueError("Invalid Name!!")
        self._name = value
    
    @name.deleter
    def name(self):
	    del self._name

if __name__ == '__main__':
    person1 = Employee('Gopi') # Provide the name in the constructor
    print(person1.name)

    person1.name = "Iyer" #Set the value
    print(person1.name)


    #person1.name = "1" #Validates the names and throws exception
    

    del person1.name # Deletes the name property; 
    # Throws an exception when  accessed after deletion
    print(person1.name)
    
    del person1
