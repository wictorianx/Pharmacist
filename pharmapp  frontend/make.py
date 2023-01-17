import random
import datetime
import json
import ast

results = {}
drugs = [
"Coraspin",
"Dolorex",
"Parol",
"Arveles",
"Dolven",
"Lansor",
"Nexium",
"Nootropil",
"Calpol",
"Aferin",
"Selectra",
"Onceair",
"Ventolin"
] 
def chanceSetup(length):
    chances = []
    for i in range(length):
        chances.append(random.randint(0, 100))
    return chances
def tc():
    digits ="1234567890"
    x=""
    for i in range(11):
        x+=random.choice(digits)
    return x
months = [31,28,31,30,31,30,31,31,30,31,30,31]
def location():
    x = random.randint(0,10000)
    y = random.randint(0,10000)
    return (x,y)
def date():
    month = random.randint(1,12)
    day = random.randint(1,months[month-1])
    year = 2021
    datex = datetime.date(year, month, day)
    return datex.strftime("%x")
def ran():
    drug = random.choice(drugs)
    tcx = tc()
    datex = date()
    locationx = location()
    return {"drug" : drug, "locationx" : locationx, "datex" : datex, "tcx" : tcx}
def chanceDistribution(liste,distribution):
    org = liste
    res = []
    c=0
    for i in distribution:
        for t in range(i):
            res.append(org[c])
        c+=1
    return res
chances = chanceSetup(len(drugs))
drugs = chanceDistribution(drugs,chances)
def make_json():
    with open(f"results{tc()}.json","w") as f:
        for i in range(10000):
            res = ran()
            jsonx = json.dumps(res)
            f.write(jsonx+",\n")
def make_list():
    xmonths = []
    for i in range(12):
        xmonths.append({})
    for i in range(10000):
            res = ran()
            jsonx = json.dumps(res)
            drug = (json.loads(jsonx)["drug"])
            month = int((json.loads(jsonx)["datex"])[:2])
            try:
                xmonths[month-1][drug]+=1
            except:
                xmonths[month-1][drug]=1
    return(xmonths)        
def make_json2():
    xmonths = []
    for i in range(12):
        xmonths.append({})
    for i in range(10000):
        res = ran()
        jsonx = json.dumps(res)
        drug = (json.loads(jsonx)["drug"])
        month = int((json.loads(jsonx)["datex"])[:2])
        try:
            xmonths[month-1][drug]+=1
        except:
            xmonths[month-1][drug]=1
    with open(f"results_{tc()}.json","w") as f:
            f.write(str(xmonths))
def read_json(name):
    with open(name,"r") as f:
        content = (f.readlines()[0])
        convert = ast.literal_eval(content[1:len(content)-1])
        return(convert)






