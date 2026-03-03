from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

try:
    database = client.get_database("mydb")
    employees = database.get_collection("employees")

    query = { "name": "123" }
    employe = employees.find_one(query)
    print(employees.insert_one(query))

    print(employe)

    client.close()

except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)