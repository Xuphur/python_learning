import pandas as pd
from tkinter import *
from tkinter import filedialog

filePath = ""

# def playDataFrame():
#     e = df.loc[0, :]
#     print(e)


def getCsvPath():
    filePath = filedialog.askopenfilename()
    file = open(filePath, "r")
    df = pd.read_csv(filePath)
    r = df.loc[0, :]
    print(r)
    # playDataFrame()
    file.close()


def selectCSV():
    window = Tk()
    button = Button(text="Open CSV", command=getCsvPath)
    button.pack()
    window.mainloop()
    getCsvPath()


try:
    selectCSV()
    # print("Starting automated test...")
    # driver.get(url)
    # get100()
    # get200()
    # get750()
    # exportResult()
    # print("Test run successful")
    # driver.quit()

except Exception as e:
    print(e)
    # print("test failed")
    # driver.quit()
