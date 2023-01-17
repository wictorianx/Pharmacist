import prediction
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import prediction
from sklearn.preprocessing import PolynomialFeatures
import xcel
import io
data = prediction.plot_data()
arveles_sales=xcel.arveles_sales()


def linear(data):
    x = np.array(data[0]).reshape(-1,1)
    y = np.array(data[1][0]).reshape(-1,1)
    
    reg = LinearRegression().fit(x, y)
    # print(reg.score(x, y))
    # print(reg.coef_)
    # print(reg.predict(x))
    # print(x)
    Y = reg.predict(x)
    fig = plt.Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.plot(x,Y)
    axis.plot(x,y)
    axis.figure.savefig("prediction.png", dpi=300, format='png',  bbox_inches='tight')
    output = plt.io.BytesIO()
    plt.FigureCanvas(fig).print_png(output)

def polynomial_plot(data,name):
    t = []
    t2 = []
    for i in range(11):
        t.append(i+1)
    t2=t+[12]
    
    x = np.array(t).reshape(-1,1)
    y = np.array(data[:-1]).reshape(-1,1)
    t2 = np.array(t2).reshape(-1,1)
    y2= np.array(data).reshape(-1,1)
    transformer = PolynomialFeatures(degree=2, include_bias=False)
    transformer.fit(x)
    x12 = t2
    x_ = transformer.transform(x)
    t2=transformer.transform(t2)


    reg = LinearRegression().fit(x_, y)
    # print(reg.score(x, y))
    # print(reg.coef_)
    # print(reg.predict(x))
    # print(x)
    Y = reg.predict(t2)
    fig = plt.Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.plot(x12,Y,label="Tahmini Değer")
    axis.plot(x12,y2,label="Gerçek Değer")
    tahmini=str(Y[11][0])[:7]
    gercek=(y2[11][0])
    axis.set_xlabel(f"Aylar\nTahmin edilen değer:{tahmini} Gerçek değer:{gercek}")
    axis.set_ylabel=("İlaç Sayısı")
    axis.legend(loc='center right', bbox_to_anchor=(0.95, 0.2))
    axis.set_title("Aylık İlaç Satışı § Tahmin")
    axis.figure.savefig(f"{name}.png", dpi=300, format='png',  bbox_inches='tight')
    output = plt.io.BytesIO()
    plt.FigureCanvas(fig).print_png(output)
def polynomial(data):
    t = []
    t2 = []
    for i in range(11):
        t.append(i+1)
    t2=t+[12]
    
    x = np.array(t).reshape(-1,1)
    y = np.array(data[:-1]).reshape(-1,1)
    t2 = np.array(t2).reshape(-1,1)
    y2= np.array(data).reshape(-1,1)
    transformer = PolynomialFeatures(degree=2, include_bias=False)
    transformer.fit(x)
    x12 = t2
    x_ = transformer.transform(x)
    t2=transformer.transform(t2)


    reg = LinearRegression().fit(x_, y)
    # print(reg.score(x, y))
    # print(reg.coef_)
    # print(reg.predict(x))
    # print(x)
    Y = reg.predict(t2)
    
    tahmini=float(str(Y[11][0])[:7])
    gercek=(y2[11][0])
    return (tahmini,gercek)
    
def predict(x,y):
   fig = plt.Figure()
   axis = fig.add_subplot(1, 1, 1)
   #xs = np.random.rand(100)
   #ys = np.random.rand(100)
   data = prediction.plot_data()
   labels = data[2]
   for i in range(13):
    a = axis.plot(x[0:12], y[i][0:12], label=labels[i])
    axis.plot(x[11:13], y[i][11:13], "--", color =a[0].get_color())
   axis.legend(loc='center right', bbox_to_anchor=(1.3, 0.5))
   axis.set_xlabel("Aylar")
   axis.set_ylabel("İlaç Kullanımı")
   axis.set_title("Aylık İlaç Kullanımı & Tahmin")
   axis.figure.savefig("prediction.png", dpi=300, format='png',  bbox_inches='tight')
   output = plt.io.BytesIO()
   plt.FigureCanvas(fig).print_png(output)
   #return Response(output.getvalue(), mimetype='image/png')




# polynomial(xcel.parol_sales(),"parol_prediction")

# linear(data)
