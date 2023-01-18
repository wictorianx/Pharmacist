import numpy as np
from sklearn.linear_model import LinearRegression
import make
import json
import ast
import matplotlib.pyplot as plt

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
#result = make.make_list()

#resultx = 
def predict(drug_name):
    ary = []
    for i in range(12):
        a = [i+1]
        print((result[i]))
        try:
            a.append(result[i][drug_name])
        except:
            a.append(0)
        ary.append(a)
    print(np.array(ary))

def pred(monthid,listx):
    result= listx
    drugs = result[monthid].keys()
    last3 = [monthid-1,monthid-2,monthid-3]
    for i in range(len(last3)):
        if last3[i]<0:
            last3[i]+=12
    avgs = {}
    
    for drug in drugs:
        avg=0
        for i in last3:
            avg+=result[i][drug]
        avg/=3
        avgs[drug]=avg
    return(avgs)
def merge(x, y):
    """Given two dictionaries, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z
def ctx(x):
    return(x[1:len(x)-1])
result = make.read_json("results_48157563556.json")
output = pred(1,result)

res =f"{result}"

o = f"{output}"
test = ast.literal_eval(res[1:len(res)-1])
# print(test)
# print(len(test))
res = ast.literal_eval(res[1:len(res)-1]+","+o)
#print(len(res))
new_dict = {}
for i in drugs:
    new_dict[i]=[]
    for t in res:
        try:
            new_dict[i].append(t[i])
        except:
            new_dict[i].append(0)

def plot():
    x=[1,2,3,4,5,6,7,8,9,10,11,12,13]
    for i in new_dict.keys():
        val = (new_dict[i])
        print(i, val)
        a = plt.plot(x[0:12], val[0:12], label=i)
        plt.plot(x[11:13], val[11:13], "--", color =a[0].get_color())
        print(a[0].get_color())
    plt.legend()
    plt.show()
def plot_data():
    x=[1,2,3,4,5,6,7,8,9,10,11,12,13]
    y = []
    labels = []
    for i in new_dict.keys():
        val = (new_dict[i])
        y.append(val)
        labels.append(i)
    return(x,y,labels)

    
#plot()