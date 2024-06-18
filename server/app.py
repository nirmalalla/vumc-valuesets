from flask import Flask, jsonify, request
from data import searchMedName
from data import associatedGroupers
from data import grabProbs
from data import probsAssociatedGroupers
from data import grabGroupersMeds
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

@app.route("/problems", methods=["GET"])
def getProblems():
    return jsonify(grabProbs())

@app.route("/problemgroupers", methods=["GET"])
def getProbGroupers():
    headers = request.headers;
    dx_id = headers.get("dx_id")
    return jsonify(probsAssociatedGroupers(dx_id))
