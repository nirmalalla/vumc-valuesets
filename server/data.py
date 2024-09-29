import json
import pandas as pd
import numpy as np
def grabMeds():
    try:
        with open("data/meds.json", "r") as file:
            data = json.load(file)
        return data

    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("error loading json")

def grabGroupers():
    try:
        with open("data/groupers.json", "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("error loading json")

def grabProbs():
    df = pd.read_csv("data/probs.txt", delimiter='\t', encoding='iso-8859-1')
    df = df.to_dict(orient="records")
    return df

def grabGroupersTxt():
    df = pd.read_csv("data/groupers.txt", delimiter='\t')
    df = df.to_dict(orient="records")
    return df

def grabGroupersMeds():
    try:
        with open("data/grouperMeds.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("error loading json")

    return data
        

def searchMedName(name, meds):
    filtered_data = list(filter(lambda med: name.upper() in med["medname"], meds))
    filtered_data = sorted(filtered_data, key= lambda med: med["patients"], reverse=True)
    return filtered_data

def associatedGroupers(med_id, groupers):
    filtered_data = list(filter(lambda grouper: "erx" in grouper and str(med_id) == str(grouper["erx"]), groupers))
    return filtered_data

def probsAssociatedGroupers(dx_id, groupers):
    filtered_groupers = []

    for grouper in groupers:
        if (str(grouper["edg"]) == dx_id):
            filtered_groupers.append(grouper)
    
    return filtered_groupers

def searchProblem(name, probs):
    filtered_data = list(filter(lambda problem: "dx_name" in problem and name in str(problem["dx_name"]), probs))
    return filtered_data

def grabGrouperProblems(name, problems, groupers):
    edgs = []

    for grouper in groupers:
        if "grouper_name" in grouper and grouper["grouper_name"] == name:
           edgs.append(str(grouper["edg"]))
    
    associatedProblems = []
    
    for problem in problems:
        if "dx_id" in problem and np.isnan(problem["dx_id"]) == False and str(int(problem["dx_id"])) in edgs:
            associatedProblems.append(problem)

    return associatedProblems 

