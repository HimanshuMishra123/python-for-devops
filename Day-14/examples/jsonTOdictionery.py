import json 
  
employee = '{"id":"09", "name": "Nitin", "department":"Finance"}' # employee is a JSON string 

employee_dict = json.loads(employee) # Convert Json string to Python dict 
print("Converted to Python", type(employee_dict)) 
print(employee_dict) 