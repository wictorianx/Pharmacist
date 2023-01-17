from flask import Flask, render_template, request
import json
import datetime
import reg 
import xcel
import bilgi
# import io
# import random
# from flask import Response
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# import numpy as np
# import make
# import prediction

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/json', methods=['GET','POST'])
def hellos():
    #return "NB"
    print(0)
    print(request.get_json())
    data = request.get_json()
    print(1)
    cart = data["cart"]
    id = data["cardid"]
    tc = data["userid"]
    price = int(data["price"])
    time = str(datetime.datetime.today())
    print(data["cardid"])
    # for i in data.keys():
    #     s+=data.i
    with open("static/cards.json", "r") as f:
        temp = json.load(f)
        temp["cards"][id]["content"] = str(int(temp["cards"][id]["content"])-price)
    with open("static/cards.json", "w") as f:
        json.dump(temp,f,indent=4)
    with open("static/sales.json", "r") as f:
        temp = json.load(f)
        
        for i in range(len(cart)):
            o = {}
            o["tc"] = tc
            o["time"] = time
            o["drug"] = cart[i]
            temp["sales"].append(o)
    with open("static/sales.json", "w") as f:
        json.dump(temp,f,indent=4)
    return "1"

@app.route('/buy')
def buy():
    
    return render_template('buy.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/prescriptions')
def prescriptions():
    return render_template('prescriptions.html')
@app.route('/prediction')
def predict():
    d = reg.polynomial(xcel.arveles_sales())
    t = d[0]
    g = d[1]
    r=t/g
    if r>2:
        bilgi.bilgilendir("Arveles")
    return render_template('prediction.html')
@app.route('/noprescription')
def fucn():
    return render_template('noprescription.html')
@app.route('/zrapor')
def func():
    return render_template('zrapor.html')