from gpay_ocr import extract_info_gpay
from db import *
import dataview
from daily_spend import draw_chart
from datetime import datetime

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

def handle_submit(name, amount, desc, category,date, time, pmode, txn_id, success, app, scroll_frame, canvas):
    users = get_users_name()
    categories = get_categories()
    user_id = None
    cat_id = None
    if name.get() in users:
        user_id = get_user_id(name.get())[0]
    else:
        create_user(name.get())
        user_id = get_user_id(name.get())[0]
    
    if category.get() in categories:
        cat_id = get_category_id(category.get())[0]
    else:
        create_category(category.get())
        cat_id = get_category_id(category.get())[0]

    add_txn(user_id, amount.get(), desc.get(), cat_id, pmode.get(), txn_id.get(), date.get() + " " + time.get())
    name.set("")
    amount.set("")
    category.set("")
    desc.set("Payment")
    date.set("")
    time.set("")
    pmode.set("")
    txn_id.set("")

    dataview.data_view(app, scroll_frame)
    success.set("Transaction Added Successfully")
    app.after(3000, lambda : success.set(""))
    draw_chart(canvas, datetime.now().strftime("%Y-%m-%d"))
    
def update_combobox(frame, combobox, callback):
    combobox['values'] = callback()
    frame.after(1000, lambda : update_combobox(frame, combobox, callback))