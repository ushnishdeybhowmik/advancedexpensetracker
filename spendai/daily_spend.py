from tkinter import Canvas
from db import get_txn_by_date

def draw_chart(canvas, date):
    # Sample data
    y = get_txn_by_date(date)
    y = [amt[0] for amt in y]   
    x = range(1,len(y)+1)
    min_y = min(y)
    max_y = max(y)
    
    #Scale data to fit chart that is 590x470 pixels
    y = [(y[i]-min_y) / (max_y - min_y) * 470 for i in range(len(y))]
    x = [i * 590 / len(x) for i in range(len(x))]

    # Draw the axes
    canvas.create_line(10, 10, 10, 480, fill="white")  # Y-axis
    canvas.create_line(10, 480, 600, 480, fill="white")  # X-axis

    # Plot the data points
    for i in range(1, len(x)):
        canvas.create_line(10 + (x[i-1]), 480 - (y[i-1]),
                           10 + (x[i]), 480 - (y[i]),
                           fill="blue", width=2)

    