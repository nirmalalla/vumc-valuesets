from flask import Flask, jsonify, request
from data import searchMedName
from data import associatedGroupers
from data import probsAssociatedGroupers
from data import grabGroupersMeds
from data import grabGrouperProblems
from data import searchProblem
from data import grabGroupers
from data import grabGroupersTxt
from data import grabMeds
from data import grabProbs
from data import grabGroupersMeds

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

groupersTxt = None
groupersJson = None
problems = None
meds = None
grouperMeds = None


def run_on_startup():
    global groupersTxt, groupersJson, problems, meds, grouperMeds

    groupersTxt = grabGroupersTxt()
    groupersJson = grabGroupers()
    problems = grabProbs()
    meds = grabMeds()
    grouperMeds = grabGroupersMeds()

run_on_startup()

@app.route("/medname", methods=["GET"])
def searchByMedname():
    headers = request.headers
    medname = headers.get("medname")
    return jsonify(searchMedName(medname, meds))

@app.route("/grouper", methods=["GET"])
def getGroupers():
    headers = request.headers
    med_id = headers.get("medication_id")
    return jsonify(associatedGroupers(med_id, groupersJson))

@app.route("/groupermeds", methods=["GET"])
def grabGrouperMeds():
    headers = request.headers
    name = headers.get("grouper_name")
    return jsonify(grouperMeds[name])

@app.route("/problemgroupers", methods=["GET"])
def getProbGroupers():
    headers = request.headers
    dx_id = headers.get("dx_id")
    return jsonify(probsAssociatedGroupers(dx_id, groupersTxt))

@app.route("/problems", methods=["GET"])
def getProbs():
    headers = request.headers
    name = headers.get("problem_name")
    return jsonify(searchProblem(name, problems))

@app.route("/grouperproblems", methods=["GET"])
def getGrouperProbs():
    headers = request.headers
    name = headers.get("name")
    return jsonify(grabGrouperProblems(name, problems, groupersTxt))