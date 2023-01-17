import pandas as pd
 
# read by default 1st sheet of an excel file
def arveles_sales():
    dataframe1 = pd.read_excel('static/arveles_sales.xls')
    months=[]
    for i in range(12):
        months.append(0)
    for i in range(len(dataframe1["Satış Tarihi"])):
        try:
            year = int(str(dataframe1["Satış Tarihi"][i])[:4])
        except:
            print(dataframe1["Satış Tarihi"][i])
        if year == 2023:
            continue
        month=int(str(dataframe1["Satış Tarihi"][i])[5:7])
        # print(dataframe1['Satış Tarihi'][i])
        count=int(dataframe1["Miktar"][i])
        months[month-1]+=count

    return months
def parol_sales():
    dataframe1 = pd.read_excel('static/PAROL.xls')
    months=[]
    for i in range(12):
        months.append(0)
    for i in range(len(dataframe1["Satış Tarihi"])):
        try:
            year = int(str(dataframe1["Satış Tarihi"][i])[:4])
        except:
            print(dataframe1["Satış Tarihi"][i])
        if year == 2023:
            continue
        try:
            month=int(str(dataframe1["Satış Tarihi"][i])[5:7])
        except:
            print(dataframe1["Satış Tarihi"][i])
            continue
        # print(dataframe1['Satış Tarihi'][i])
        count=int(dataframe1["Miktar"][i])
        months[month-1]+=count

    return months


#Tarih Miktar