from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = Flask(__name__)

# TODO:
# restriction: authorised only
# restriction: only allow required parameters to be posted


@app.route("/members", methods=["GET", "POST"])
def members():
    if request.method == "GET":
        with open(os.getenv("DATA"), "r") as file:
            data = json.load(file)

            return jsonify(data), 200
    elif request.method == "POST":
        # restriction: parameters required
        if not all(key in request.json for key in ("name", "picture")):
            return jsonify({"message": "name and picture parameters are required"}), 400

        # resriction: parameters length
        if len(request.json["name"]) < 3 or len(request.json["name"]) > 32:
            return jsonify({"message": "name parameter must be between 3 and 32 characters"}), 400

        if "bio" in request.json and len(request.json["bio"]) > 512:
            return jsonify({"message": "bio parameter must be less than 512 characters"}), 400

        if "bio" not in request.json:
            request.json["bio"] = "This member has not yet set a bio."

        with open(os.getenv("DATA"), "r") as file:
            data = json.load(file)

        # resriction: name duplicate
        for member in data["members"]:
            if member["name"] == request.json["name"]:
                return jsonify({"message": "name is already taken"}), 400

        data["members"].append(request.json)

        with open(os.getenv("DATA"), "w") as file:
            json.dump(data, file)

        return jsonify({"message": "successfully added member"}), 201


@ app.errorhandler(404)
def not_found(e):
    return jsonify({"message": "route not found"}), 404


@ app.errorhandler(405)
def not_allowed(e):
    return jsonify({"message": "method not allowed"}), 405


if __name__ == "__main__":
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"), debug=os.getenv("DEBUG"))
