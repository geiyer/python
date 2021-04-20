import unittest
import json
from class_definitions import json_transform as t

class JSONTransform(unittest.TestCase):
    def setUp(self):        
        self.json_in = '''
                {
                    "employees": [
                        {
                            "EMP_ID": 12786,
                            "EMP_NAME": "Jill Jackson",
                            "EMP_DEPT": "Finance"
                            
                        },
                        {
                            "EMP_ID": 106836932,
                            "EMP_NAME": "Tom Harvey",
                            "EMP_DEPT": "Marketing"
                            
                        }
                    ]
                }
            '''

    
    def test_structure(self):
        json_out = '''
                {
                    "employees": [
                        {
                            "employee_id": 12786,
                            "full_name": "Jill Jackson",
                            "department": "Finance"
                        },
                        {
                            "employee_id": 106836932,
                            "full_name": "Tom Harvey",
                            "department": "Marketing"
                        }
                    ]
                }
            '''
        self.assertEqual(t.transform(self.json_in), json.loads(json_out))

if __name__ == '__main__':
    unittest.main()