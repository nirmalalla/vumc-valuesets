import json
import pandas as pd

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

def grabGroupersMeds(name):
    try:
        with open("data/grouperMeds.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("error loading json")

    return data[name]
        

def searchMedName(name):
    meds = grabMeds()
    filtered_data = list(filter(lambda med: name.upper() in med["medname"], meds))
    filtered_data = sorted(filtered_data, key= lambda med: med["patients"], reverse=True)
    return filtered_data

def associatedGroupers(med_id):
    groupers = grabGroupers()
    filtered_data = list(filter(lambda grouper: "erx" in grouper and med_id == grouper["erx"], groupers))
    return filtered_data

def probsAssociatedGroupers(dx_id):
    groupers = grabGroupersTxt()
    groupers = list(filter(lambda grouper: grouper["edg"] == dx_id, groupers))
    return groupers

def searchProblem(name):
    probs = grabProbs()
    filtered_data = list(filter(lambda problem: "dx_name" in problem and name in str(problem["dx_name"]), probs))
    return filtered_data