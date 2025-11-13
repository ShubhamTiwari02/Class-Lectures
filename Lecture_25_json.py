#JSON - JavaScript Object Notation, used for data interchange (data storage and exchange)
#import json
#x = {"id": "unique-identifier","firstName": "John","lastName": "Doe","dateOfBirth": "1990-01-15","email": "john.doe@example.com","phone": "+1-555-0123","address": {"street": "123 Main St","city": "Springfield","state": "IL","zipCode": "62701","country": "USA"},"gender": "Male","nationality": "American","occupation": "Software Engineer","company": "Tech Solutions","skills": ["Python","JavaScript","SQL","HTML","CSS"],"languages": ["English","Spanish"],"maritalStatus": "Single","children": 0,"hobbies": ["Reading","Traveling","Gaming"],"website": "http://johndoe.com","socialMedia": {"linkedin": "linkedin.com/in/johndoe","twitter": "@johndoe"}}
#y = json.loads(x) #Converts JSON string to Python dictionary
#print(y["email"])
#-------------------------------------------------------------------------------
'''x = {
    "id": "unique-identifier",
    "firstName": "John",
    "lastName": "Doe",
    "dateOfBirth": "1990-01-15",
    "email": "john.doe@example.com",
    "phone": "+1-555-0123",
    "address": {
        "street": "123 Main St",
        "city": "Springfield",
        "state": "IL",
        "zipCode": "62701",
        "country": "USA"
    },
    "gender": "Male",
    "nationality": "American"
}
y = json.dumps(x) #Converts Python dictionary to JSON string
print(type(y))

print("---------------------------------------------------")
print(json.dumps({"name": "John", "age": 30}))
print("---------------------------------------------------")
print(json.dumps(["apple", "bananas"]))
print("---------------------------------------------------")
print(json.dumps(("apple", "bananas")))
print("---------------------------------------------------")
print(json.dumps("hello"))
print("---------------------------------------------------")
print(json.dumps(42))
print("---------------------------------------------------")
print(json.dumps(31.76))
print("---------------------------------------------------")
print(json.dumps(True))
print("---------------------------------------------------")
print(json.dumps(False))
print("---------------------------------------------------")
print(json.dumps(None))
print("---------------------------------------------------")'''
#y = json.dumps(x, indent=4, separators=(", ", " = ")) #Pretty print JSON with custom separators
#print(y)

