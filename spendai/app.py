from ttkbootstrap import Window, Combobox
from tkinter.ttk import Frame, Label, Entry, Button
from tkinter import filedialog, StringVar, IntVar
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from db import get_users_name, get_categories
from tools import update_combobox, upload_file, handle_submit
from datetime import datetime
from dataview import data_view

# Get the path to the logo
logo_path = "spendai/assets/logo.ico"

app = Window(themename="vapor")
app.geometry("1920x1080")
app.title("spend.ai")
app.iconbitmap(logo_path)

colors = app.style.colors

input_frame = Frame(app, bootstyle=DARK)
input_frame.place(x=0, y=0, width=500, height=1080)

input_label_var_description = StringVar(input_frame, "Payment")
input_label_description = Label(input_frame, text="Description", font=("Segoe UI", 8, "bold"), background=colors.dark)
input_label_description.place(x=20, y=20, width = 100, height=20)
input_entry_description =Entry(input_frame, textvariable=input_label_var_description)
input_entry_description.place(x=140, y=20, width=320)

input_label_var_amount = IntVar(input_frame, 0)
input_label_amount = Label(input_frame, text="Amount", font=("Segoe UI", 8, "bold"), background=colors.dark)
input_label_amount.place(x=20, y=60, width = 100, height=20)
input_entry_amount =Entry(input_frame, textvariable=input_label_var_amount)
input_entry_amount.place(x=140, y=60, width=320)

input_label_var_pmode = StringVar(input_frame, "UPI")
input_label_pmode = Label(input_frame, text="Payment Mode", font=("Segoe UI", 8, "bold"), background=colors.dark)
input_label_pmode.place(x=20, y=100, width = 100, height=20)
input_entry_pmode = Combobox(input_frame, bootstyle=DARK, textvariable=input_label_var_pmode, values=["UPI", "Debit Card", "Cash"])
input_entry_pmode.place(x=140, y=100, width=320)

user_names = get_users_name()

input_label_var_person = StringVar(input_frame, "")
input_label_person = Label(input_frame, text="To", font=("Segoe UI", 8, "bold"), background=colors.dark)
input_label_person.place(x=20, y=140, width = 100, height=20)
input_entry_person = Combobox(input_frame, bootstyle=DARK, textvariable=input_label_var_person, values=user_names)
input_entry_person.place(x=140, y=140, width=320)
update_combobox(input_frame, input_entry_person, get_users_name)

input_label_var_date = StringVar(input_frame, str(datetime.now().strftime("%Y-%m-%d")))
input_label_date = Label(input_frame, text="Date", font=("Segoe UI", 8, "bold"), background=colors.dark)
input_label_date.place(x=20, y=180, width = 100, height=20)
input_entry_date = Entry(input_frame, textvariable=input_label_var_date)
input_entry_date.place(x=140, y=180, width=320)

input_label_var_time = StringVar(input_frame, str(datetime.now().strftime("%H:%M:%S")))
input_label_time = Label(input_frame, text="Time", font=("Segoe UI", 8, "bold"), background=colors.dark)
input_label_time.place(x=20, y=220, width = 100, height=20)
input_entry_time = Entry(input_frame, textvariable=input_label_var_time)
input_entry_time.place(x=140, y=220, width=320)

input_var_txn = StringVar(input_frame, "")
input_label_txn = Label(input_frame, text="Txn ID", font=("Segoe UI", 8, "bold"), background=colors.dark)
input_label_txn.place(x=20, y=260, width = 100, height=20)
input_entry_txn = Entry(input_frame, textvariable=input_var_txn)
input_entry_txn.place(x=140, y=260, width=320)

categories = get_categories()

input_var_category = StringVar(input_frame, "")
input_label_category = Label(input_frame, text="Category", font=("Segoe UI", 8, "bold"), background=colors.dark)
input_label_category.place(x=20, y=300, width = 100, height=20)
input_entry_category = Combobox(input_frame, bootstyle=DARK, textvariable=input_var_category, values=user_names)
input_entry_category.place(x=140, y=300, width=320)
update_combobox(input_frame, input_entry_category, get_categories)

input_label_OR = Label(input_frame, text="OR", font=("Segoe UI", 8, "bold"), background=colors.dark)
input_label_OR.place(x=200, y=370, width = 100, height=20)

input_label_gpay = Label(input_frame, text="Upload GPAY Receipt", font=("Segoe UI", 8, "bold"), background=colors.dark)
input_label_gpay.place(x=20, y=410, width = 150, height=20)
file_path = StringVar(input_frame, "No File Selected")
btn_upload = Button(input_frame, text="Upload File", command=lambda : upload_file(filedialog, file_path,input_label_var_person, input_label_var_amount, input_label_var_date, input_label_var_time, input_label_var_pmode, input_var_txn))
btn_upload.place(x=190, y=410, width=260, height=35)
file_label = Label(input_frame, textvariable=file_path, font=("Segoe UI", 8, "bold"), foreground='#FFFFFF', background=colors.dark)
file_label.place(x=20, y=450, width = 460, height=20)

success = StringVar(input_frame, "")
submit_btn = Button(input_frame, text="Submit", command=lambda : handle_submit(input_label_var_person, input_label_var_amount, input_label_var_description, input_var_category, input_label_var_date, input_label_var_time, input_label_var_pmode, input_var_txn, success, app, scroll_frame))
submit_btn.place(x=20, y=490, width=460, height=35)

success_label = Label(input_frame, textvariable=success, font=("Segoe UI", 8, "bold"), foreground='#00FF00', background=colors.dark)
success_label.place(x=20, y=530, width = 460, height=20)

scroll_frame = ScrolledFrame(app, height=540, width=1420)
scroll_frame.place(x=500, y=0)
data_view(app, scroll_frame)


app.mainloop()  