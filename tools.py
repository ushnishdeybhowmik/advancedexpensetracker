from gpay_ocr import extract_info_gpay
from db import *
import dataview

def upload_file(filedialog, label_file_path, name, amount, date, time, pmode, txn_id):
    # Open a file dialog to select a file
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=(("Image files", "*.png;*.jpg;*.jpeg"),  # Filter for text files
                   ("All files", "*.*"))    # Allow all files
    )
    
    if file_path:
        pic = file_path.split('/')[-1]
        label_file_path.set(f'Selected File: {pic}' if file_path else 'No File Selected')
        info = extract_info_gpay(file_path)
        name.set(info[0])
        amount.set(info[1])
        date.set(info[2])
        time.set(info[3])
        pmode.set(info[4])
        txn_id.set(info[5])

def handle_submit(name, amount, desc, date, time, pmode, txn_id, success, app, scroll_frame):
    users = get_users_name()
    if name.get() in users:
        add_txn(get_user_id(name.get())[0], amount.get(), desc.get(), pmode.get(), txn_id.get(), date.get() + " " + time.get())
        name.set("")
        amount.set("")
        desc.set("")
        date.set("")
        time.set("")
        pmode.set("")
        txn_id.set("")
    else:
        create_user(name.get())
        add_txn(get_user_id(name.get())[0], amount.get(), desc.get(), pmode.get(), txn_id.get(), date.get() + " " + time.get())
        name.set("")
        amount.set("")
        desc.set("")
        date.set("")
        time.set("")
        pmode.set("")
        txn_id.set("")

    dataview.data_view(app, scroll_frame)
    success.set("Transaction Added Successfully")
    
def update_combobox(frame, combobox):
    combobox['values'] = get_users_name()
    frame.after(1000, lambda : update_combobox(frame, combobox))