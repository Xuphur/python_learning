import pandas as pd
from tkinter import *
from tkinter import filedialog


city = "pheonix"
state = "AZ"


def exportResult(r):
    try:
        data = pd.DataFrame(r)
        d = data.dropna().drop_duplicates()
        print(len(d), city)
        filename = str(city) + str(state) + "- final.csv"
        d.to_csv(filename, mode="a", index=False, header=False)
    except Exception as e:
        print(e)


def getCsv():
    try:
        filePath = ""
        filePath = filedialog.askopenfilename()
        file = open(filePath, "r")
        df = pd.read_csv(filePath)
        file.close()
        print(df)
        exportResult(df)
    except Exception as e:
        print(e)


try:
    getCsv()

except:
    print("error")
