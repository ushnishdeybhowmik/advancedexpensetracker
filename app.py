import tkinter as tk 
from tkinter import ttk
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from db import *
import datetime as dt

create_user_table()

app = ttkb.Window(themename="vapor")
app.geometry("1920x1080")
app.title("spend.ai")
app.iconbitmap('logo.ico')

colors = app.style.colors

input_frame = ttk.Frame(app, bootstyle=DARK)
input_frame.place(x=0, y=0, width=500, height=1080)

input_label_var_description = tk.StringVar(input_frame, "Payment")
input_label_description = ttk.Label(input_frame, text="Description", font=("Segoe UI", 8, "bold"), background=colors.dark)
input_label_description.place(x=20, y=20, width = 100, height=20)
input_entry_description = ttk.Entry(input_frame, textvariable=input_label_var_description)
input_entry_description.place(x=140, y=20, width=320)

input_label_var_amount = tk.IntVar(input_frame, 0)
input_label_amount = ttk.Label(input_frame, text="Amount", font=("Segoe UI", 8, "bold"), background=colors.dark)
input_label_amount.place(x=20, y=60, width = 100, height=20)
input_entry_amount = ttk.Entry(input_frame, textvariable=input_label_var_amount)
input_entry_amount.place(x=140, y=60, width=320)

input_label_var_pmode = tk.StringVar(input_frame, "UPI")
input_label_pmode = ttk.Label(input_frame, text="Payment Mode", font=("Segoe UI", 8, "bold"), background=colors.dark)
input_label_pmode.place(x=20, y=100, width = 100, height=20)
input_entry_pmode = ttkb.Combobox(input_frame, bootstyle=DARK, textvariable=input_label_var_pmode, values=["UPI", "Debit Card", "Cash"])
input_entry_pmode.place(x=140, y=100, width=320)

user_names = get_users_name()

input_label_var_person = tk.StringVar(input_frame, "")
input_label_person = ttk.Label(input_frame, text="To", font=("Segoe UI", 8, "bold"), background=colors.dark)
input_label_person.place(x=20, y=140, width = 100, height=20)
input_entry_person = ttkb.Combobox(input_frame, bootstyle=DARK, textvariable=input_label_var_person, values=user_names)
input_entry_person.place(x=140, y=140, width=320)

input_label_var_date = tk.StringVar(input_frame, str(dt.datetime.now().strftime("%Y-%m-%d")))
input_label_date = ttk.Label(input_frame, text="Date", font=("Segoe UI", 8, "bold"), background=colors.dark)
input_label_date.place(x=20, y=180, width = 100, height=20)
input_entry_date = ttk.Entry(input_frame, textvariable=input_label_var_date)
input_entry_date.place(x=140, y=180, width=320)

input_label_var_time = tk.StringVar(input_frame, str(dt.datetime.now().strftime("%H:%M:%S")))
input_label_time = ttk.Label(input_frame, text="Time", font=("Segoe UI", 8, "bold"), background=colors.dark)
input_label_time.place(x=20, y=220, width = 100, height=20)
input_entry_time = ttk.Entry(input_frame, textvariable=input_label_var_time)
input_entry_time.place(x=140, y=220, width=320)

input_label_OR = ttk.Label(input_frame, text="OR", font=("Segoe UI", 8, "bold"), background=colors.dark)
input_label_OR.place(x=200, y=290, width = 100, height=20)

app.mainloop()  