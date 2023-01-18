import json
import datetime
with open("static/cards.json", "r") as f:
    temp = json.load(f)
    temp["cards"][0]["content"] = "1000"
with open("static/cards.json", "w") as f:
    json.dump(temp,f,indent=4)
    
def salesave(id, time, cart):
    with open("static/cards.json", "r") as f:
        temp = json.load(f)
        
        for i in range(len(cart)):
            o = {}
            o["id"] = id
            o["time"] = time
            o["drug"] = cart[i]
            temp["sales"].append()
    with open("static/cards.json", "w") as f:
        json.dump(temp,f,indent=4)
        
