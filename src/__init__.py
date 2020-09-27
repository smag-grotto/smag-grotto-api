from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = Flask(__name__)

# TODO:
# restriction: authorised only
# restriction: only allow required parameters to be posted


@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        with open(os.getenv("DATA"), "r") as file:
            data = json.load(file)

            return jsonify(data), 200
    elif request.method == "POST":
        # restriction: parameter(s) required
        if not all(key in request.json for key in ("name", "picture", "bio")):
            return jsonify({"message": "all parameters are required: name, picture, bio"}), 400

        # resriction: parameter(s) length
        if len(request.json["name"]) < 3 or len(request.json["name"]) > 32:
            return jsonify({"message": "name parameter must be between 3 and 32 characters"}), 400

        if len(request.json["bio"]) < 3 or len(request.json["bio"]) > 512:
            return jsonify({"message": "bio parameter must be between 3 and 512 characters"}), 400

        with open(os.getenv("DATA"), "r") as file:
            data = json.load(file)

        # resriction: name duplicate
        for user in data["users"]:
            if user["name"] == request.json["name"]:
                return jsonify({"message": "name is already taken"}), 400

        data["users"].append(request.json)

        with open(os.getenv("DATA"), "w") as file:
            json.dump(data, file)

        return jsonify({"message": "successfully added user"}), 201


@ app.errorhandler(404)
def not_found(e):
    return jsonify({"message": "route not found"}), 404


@ app.errorhandler(405)
def not_allowed(e):
    return jsonify({"message": "method not allowed"}), 405


if __name__ == "__main__":
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"), debug=os.getenv("DEBUG"))
