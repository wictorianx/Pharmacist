import matplotlib.pyplot as plt
import prediction
def predict():
   fig = plt.Figure()
   axis = fig.add_subplot(1, 1, 1)
   #xs = np.random.rand(100)
   #ys = np.random.rand(100)
   data = prediction.plot_data()
   x = data[0]
   y = data[1]
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
predict()