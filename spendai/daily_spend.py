from tkinter import Canvas
from db import get_txn_by_date

def draw_chart(canvas, date):
    # Sample data
    y = get_txn_by_date(date)
    y = [amt[0] for amt in y]   
    x = range(1,len(y)+1)
    min_y = min(y)
    max_y = max(y)
    
    margin = 40
    height = 500 - 2*margin
    width = 710 - 2*margin
    
    #Scale data to fit chart that is 590x470 pixels
    y = [(y[i]-min_y) / (max_y - min_y) * height for i in range(len(y))]
    x = [i * width / len(x) for i in range(len(x))]

    # Draw the axes
    canvas.create_line(margin, margin, margin, height+margin, fill="#320459")  # Y-axis
    canvas.create_line(margin, height+margin, margin + width, height+margin, fill="#320459")  # X-axis
    j = 0
    for i in range(10, -1, -1):
        canvas.create_text(margin - 20, margin + (i*(height/10)), text=str(min_y + j*(max_y - min_y)/10), fill="#824be3", font=("Segoe UI", 8))
        if i != 10:
            canvas.create_line(margin, margin + (i*(height/10)), margin + width, margin + (i*(height/10)), fill="#320459", dash=(2, 2))
        j += 1
    # Plot the data points
    for i in range(1, len(x)):
        canvas.create_line(margin + (x[i-1]), margin+height - (y[i-1]),
                           margin + (x[i]), margin+height - (y[i]),
                           fill="#824be3", width=2)

    