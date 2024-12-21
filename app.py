import tkinter as tk 
from tkinter import ttk
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

app = ttkb.Window(themename="vapor")
app.geometry("1920x1080")
app.title("spend.ai")
app.iconbitmap('logo.ico')

colors = app.style.colors

input_frame = ttk.Frame(app, bootstyle=DARK)
input_frame.place(x=0, y=0, width=500, height=1080)

input_label_var_description = tk.StringVar(input_frame, "Payment")
input_label_description = ttk.Label(input_frame, text="Description", font=("Segoe UI", 8, "bold"))
input_label_description.place(x=20, y=20, width = 100, height=20)
input_entry_description = ttk.Entry(input_frame, textvariable=input_label_var_description)
input_entry_description.place(x=140, y=20, width=320)

input_label_var_amount = tk.IntVar(input_frame, 0)
input_label_amount = ttk.Label(input_frame, text="Amount", font=("Segoe UI", 8, "bold"))
input_label_amount.place(x=20, y=60, width = 100, height=20)
input_entry_amount = ttk.Entry(input_frame, textvariable=input_label_var_amount)
input_entry_amount.place(x=140, y=60, width=320)

input_label_var_pmode = tk.StringVar(input_frame, "UPI")
input_label_pmode = ttk.Label(input_frame, text="Payment Mode", font=("Segoe UI", 8, "bold"))
input_label_pmode.place(x=20, y=100, width = 100, height=20)
input_entry_pmode = ttkb.Combobox(input_frame, bootstyle=DARK, textvariable=input_label_var_pmode, values=["UPI", "Debit Card", "Cash"])
input_entry_pmode.place(x=140, y=100, width=320)




app.mainloop()  