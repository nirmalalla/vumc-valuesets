from flask import Flask, jsonify, request
from data import searchMedName
from data import associatedGroupers
from data import probsAssociatedGroupers
from data import grabGroupersMeds
from data import searchProblem
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/medname", methods=["GET"])
def searchByMedname():
    headers = request.headers
    medname = headers.get("medname")
    return jsonify(searchMedName(medname))

@app.route("/grouper", methods=["GET"])
def getGroupers():
    headers = request.headers
    med_id = headers.get("medication_id")
    return jsonify(associatedGroupers(med_id))

@app.route("/groupermeds", methods=["GET"])
def grabGrouperMeds():
    headers = request.headers
    name = headers.get("grouper_name")
    return jsonify(grabGroupersMeds(name))

@app.route("/problemgroupers", methods=["GET"])
def getProbGroupers():
    headers = request.headers
    dx_id = headers.get("dx_id")
    return jsonify(probsAssociatedGroupers(dx_id))

@app.route("/problems", methods=["GET"])
def getProbs():
    headers = request.headers
    name = headers.get("problem_name")
    return jsonify(searchProblem(name))
