

from flask import Flask, jsonify
from pymongo import AsyncMongoClient

app = Flask(__name__)

 # type: ignore
@app.route("/")
def work():
    return "work!!"

@app.route('/employees', methods=['post'])
async def creationcompte():
    uri = "mongodb://localhost:27017/"
    client = AsyncMongoClient(uri)
    try:
        database = client.get_database("mydb")
        employees = database.get_collection("employees")
        
        query = { "nom": "123" }
        employe = await employees.find_one(query)
        return jsonify({"200"})
        await client.close()
    except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)
if __name__ == "__main__":
    app.run(debug=True) # type: ignore
    
#flask response for eitheir
    #response = flask.make_response(something)
    #response.headers['content-type'] = 'application/octet-stream'
    #return response