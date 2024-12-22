from ttkbootstrap.tableview import Tableview
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.constants import *
from db import get_txn_columns, get_all_txn_with_names

def data_view(master, scroll_frame : ScrolledFrame):
    

    colors = master.style.colors
    coldata = get_txn_columns()
    rowdata = get_all_txn_with_names()
    col_meta = []
    for col in coldata:
        col_meta.append({
            "text" : col,
            "stretch" : True
            })
                
    dt = Tableview(
        master=scroll_frame,
        coldata=col_meta,
        rowdata=rowdata,
        paginated=True,
        pagesize=19,
        searchable=True,
        bootstyle=PRIMARY
    )
    dt.place(x=0, y=0, height=540, width=1420)