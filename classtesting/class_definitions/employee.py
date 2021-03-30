from .person import Person

class Employee(Person):
    '''Employee Class derives from Person'''
        # Constructor
    def __init__(self, lname, fname, ssn, dept, empId):
        super().__init__(lname, fname, ssn)
        self.department = dept
        self.ID = empId

    #Method overriding: changing the behaviour of the method 
    def display(self): 
        return str(super().display()) + "\nDepartment: " + str(self.department) + " Emp ID:  " + str(self.ID) 


