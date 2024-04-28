from tkinter import *
from tkinter import messagebox
from joblib import load
import numpy as np

regr = load("mlp.joblib")
scaler = load("scaler_x.joblib")
root = Tk()
root.title('Predict Value')
root.resizable(0,0)

tempL = Label(root, text = "Temp(C)")
humL = Label(root, text = "Hum(%)")
pressL = Label(root, text = "Press(hPa)")
noL = Label(root, text = "NO(ug/m3)")
no2L = Label(root, text = "NO2(ug/m3)")
ozoneL = Label(root, text = "Ozone(ug/m3)")
pm10L = Label(root, text = "RM10(ug/m3)")

nonormL = Label(root, text = "NO/NO2 norm is:%d" % 200)
o3normL = Label(root, text = "O3 norm is:%d" % 200)
pm10normL = Label(root, text = "RM10 norm is:%d" % 50)

tempE = Entry(root)
humE = Entry(root)
pressE = Entry(root)
noE = Entry(root)
no2E = Entry(root)
ozoneE = Entry(root)
pm10E = Entry(root)

tempL.grid(row=0)
tempE.grid(row=0, column=1)

humL.grid(row=1)
humE.grid(row=1, column=1)

pressL.grid(row=2)
pressE.grid(row=2, column=1)

noL.grid(row=3)
noE.grid(row=3, column=1)
nonormL.grid(row=3, column=2)

no2L.grid(row=4)
no2E.grid(row=4, column=1)

ozoneL.grid(row=5)
ozoneE.grid(row=5, column=1)
o3normL.grid(row=5, column=2)

pm10L.grid(row=6)
pm10E.grid(row=6, column=1)
pm10normL.grid(row=6, column=2)

def Predict():
    noE.delete(0,END)
    no2E.delete(0,END)
    ozoneE.delete(0,END)
    pm10E.delete(0,END)
    try:
        arr = np.array([[float(tempE.get()),float(humE.get()),float(pressE.get())]])
        arr_transformed = scaler.transform(arr)
        pr = regr.predict(arr_transformed)
        noE.insert(0,round(pr[0][0],2))
        no2E.insert(0,round(pr[0][1],2))
        ozoneE.insert(0,round(pr[0][2],2))
        pm10E.insert(0,round(pr[0][3],2))
    except ValueError:
        messagebox.showinfo("Wrong Value", "Please enter float values!")
        
b = Button(root, text="Predict", command=Predict)

b.grid(row=7)

root.mainloop()
        




    
