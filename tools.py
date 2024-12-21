from gpay_ocr import extract_info_gpay

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
