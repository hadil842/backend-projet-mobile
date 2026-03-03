from flask import Flask, jsonify, request
from motor.motor_asyncio import AsyncIOMotorClient 
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

uri = "mongodb://localhost:27017/"
client = AsyncIOMotorClient(uri)  
database = client.get_database("mydb")
users = database.get_collection("client")
freelancer= database.get_collection("freelancer")

@app.route('/signclient', methods=['POST'])
async def creationcompteclient():
    try:
        data = request.get_json()
        newuser = {
            "nom": data.get("nom"),
            "prenom": data.get("prenom"),
            "email": data.get("email"),
            "password": generate_password_hash(data.get("password")),
            "profession": data.get("profession"),
            "status": "encours"
        }
        
        result = await users.insert_one(newuser)
        return jsonify({"message": "user added"}), 201
        
    except Exception as e:
        return jsonify({"error":"error signing up", "details": str(e)}), 500

@app.route('/loginclient', methods=['POST'])
async def loginclient():
    try:
        data = request.get_json()
        user = {"nom": data.get("nom")}
        
        result = await users.find_one(user)
        
        if result is None:
            return jsonify({"message": "user not found"}), 404
        
        if check_password_hash(result.get("password"),data.get("password")):
            return jsonify({"message": "login successful"}), 200
        else:
            return jsonify({"message": "invalid password"}), 401

    except Exception as e:
        return jsonify({'error':str(e)}), 500

@app.route('/signfreelancer', methods=['POST'])
async def creationcomptefreelancer():
    try:
        data = request.get_json()
        newfree = {
            "nom": data.get("nom"),
            "prenom": data.get("prenom"),
            "email": data.get("email"),
            "password": generate_password_hash(data.get("password")),
            "profession": data.get("profession"),
            "status": "encours",
            "bio":data.get("bio"),
            "competances":data.get("competances"),
            "cv":data.get("cv"),
            "portfolio":data.get("portfolio")
        }
        
        result = await freelancer.insert_one(newfree)
        return jsonify({"message": "freelancer added"}), 201
        
    except Exception as e:
        return jsonify({"error":"error signing up", "details": str(e)}), 500
@app.route('/loginfreel', methods=['POST'])
async def loginfreel():
    try:
        data = request.get_json()
        freel = {"nom": data.get("nom")}
        
        result = await freelancer.find_one(freel)
        
        if result is None:
            return jsonify({"message": "freelancer not found"}), 404
        
        if check_password_hash(result.get("password"),data.get("password")):
            return jsonify({"message": "login successful"}), 200
        else:
            return jsonify({"message": "invalid password"}), 401

    except Exception as e:
        return jsonify({'error':str(e)}), 500
if __name__ == "__main__":
    app.run(debug=True)
