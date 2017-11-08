import tkinter as tk
import tkinter.ttk as ttk
import smtplib as smtp
import email.mime as email

#constants
myfont=("Courier New", 12)

def send_mail():
    print ("Mail sent")

window = tk.Tk()
window.title("Email application")
window.geometry("840x625")
toLabel = tk.Label(window, text="To:    ")
toLabel.grid(row=0,column=0,sticky=tk.E)

varTo = tk.StringVar(window, value="address@email.com")

toBox = ttk.Combobox(window, textvariable=varTo, font=myfont, width=40)
toBox.grid(row=0,column=8, sticky=tk.W)

toLabel = tk.Label(window, text="From:  ")
toLabel.grid(row=1,column=0,sticky=tk.E)

varFrom = tk.StringVar(window, value="address@email.com")
varSubject = tk.StringVar(window, value="Type in a subject")

fromBox = ttk.Combobox(window, textvariable=varFrom, font=myfont, width=40)
fromBox.grid(row=1,column=8, sticky=tk.W)
fromBox['values']=('madhuja@outlook.com','madhuja.kamath@sjsu.edu','info@evilcorp.com')

mainText = tk.Text(window, font=("Arial", 14), width=70, height=20)
mainText.grid(row=6,column=8, pady=20)

sendBtn = tk.Button(window, text="Send", fg="black", bg="grey", command=send_mail)
sendBtn.grid(row=12, column=8, sticky=tk.E)
