import unittest
from class_definitions import employee as t


class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.employee = t.Employee('Duck', 'Daisy','111-11-1111', 'Sales', 1234)

    def tearDown(self):
        del self.employee

    def test_initial_value_required_attributes(self):
        self.assertEqual(self.employee.last_name, 'Duck')
        self.assertEqual(self.employee.first_name, 'Daisy')
        self.assertEqual(self.employee.department, 'Sales')
        self.assertEqual(self.employee.ID, 1234)

    def test_employee_display_method(self):
        # employee = t.Employee('Duck', 'Daisy', '111-11-1111', 'Sales', 123) # this is not self.person from setUp, but local
        # assert employee.display() == 'Duck'  
        self.assertEqual(self.employee.display(), 'Duck, Daisy\nDepartment: Sales Emp ID:  1234')

        

if __name__ == '__main__':
    unittest.main()