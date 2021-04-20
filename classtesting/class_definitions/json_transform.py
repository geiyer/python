import json

def transform (json_input):
    json_data = json.loads(json_input) 
    for key, obj in enumerate(json_data['employees']):
        newobj = {'employee_id': obj.get('EMP_ID'),
                'full_name': obj.get('EMP_NAME'), 
                'department': obj.get('EMP_DEPT')
                }         
        json_data['employees'][key] = newobj
    return json_data
