import matplotlib.pyplot as plt
import numpy as np
import ast
import tkinter as tk

# Define a function to create a custom chart
def create_chart(x, y, kind, xlabel="", ylabel="", title="", filename="chart.png"):
    plt.figure()
    if kind == "line":
        plt.plot(x, y, color="blue", linestyle="--")
    elif kind == "bar":
        plt.bar(x, y, color="green", edgecolor="black")
    elif kind == "scatter":
        plt.scatter(x, y, color="red", marker="*")
    elif kind == "hist":
        plt.hist(y, bins=x, color="purple", alpha=0.5)
    plt.xlabel(xlabel, fontdict={"family": "Arial", "size": 12})
    plt.ylabel(ylabel, fontdict={"family": "Arial", "size": 12})
    plt.title(title, fontdict={"family": "Arial", "size": 16})
    plt.savefig(filename)
    plt.show()

# Define a function to get the user input from the GUI and call the create_chart() function
def get_input():
    try:
        x = ast.literal_eval(entry_x.get())
        y = ast.literal_eval(entry_y.get())
        kind = entry_kind.get()
        xlabel = entry_xlabel.get()
        ylabel = entry_ylabel.get()
        title = entry_title.get()
        filename = entry_filename.get()
        if kind not in ["line", "bar", "scatter", "hist"]:
            raise ValueError("Invalid chart type")
    except Exception as e:
        label_error.config(text="Invalid input: " + str(e))
    else:
        label_error.config(text="")
        create_chart(x, y, kind, xlabel, ylabel, title, filename)

# Create a root window for the GUI
root = tk.Tk()
root.title("MG visualizer")

# Create a frame to hold the input widgets
frame_input = tk.Frame(root)
frame_input.pack()

# Create labels and entries for the x and y values
label_x = tk.Label(frame_input, text="Enter the x values as a list or an array:")
label_x.grid(row=0, column=0, sticky="w")
entry_x = tk.Entry(frame_input)
entry_x.grid(row=0, column=1)
entry_x.insert(0, "[1, 2, 3]") # Example input

label_y = tk.Label(frame_input, text="Enter the y values as a list or an array:")
label_y.grid(row=1, column=0, sticky="w")
entry_y = tk.Entry(frame_input)
entry_y.grid(row=1, column=1)
entry_y.insert(0, "[4, 5, 6]") # Example input

# Create labels and entries for the chart type and the labels and title
label_kind = tk.Label(frame_input,text="Enter the chart type (line , bar, scatter or hist):")
label_kind.grid(row=2, column=0, sticky="w")
entry_kind = tk.Entry(frame_input)
entry_kind.grid(row=2, column=1)
entry_kind.insert(0, "line") # Example input

label_xlabel = tk.Label(frame_input, text="Enter the x axis label:")
label_xlabel.grid(row=3, column=0, sticky="w")
entry_xlabel = tk.Entry(frame_input)
entry_xlabel.grid(row=3, column=1)

label_ylabel = tk.Label(frame_input, text="Enter the y axis label:")
label_ylabel.grid(row=4, column=0, sticky="w")
entry_ylabel = tk.Entry(frame_input)
entry_ylabel.grid(row=4, column=1)

label_title = tk.Label(frame_input, text="Enter the chart title:")
label_title.grid(row=5, column=0, sticky="w")
entry_title = tk.Entry(frame_input)
entry_title.grid(row=5,column=1)

# Create labels and entries for the file name
label_filename = tk.Label(frame_input,text="Enter the file name to save the chart:")
label_filename.grid(row=6,column=0,sticky="w")
entry_filename=tk.Entry(frame_input)
entry_filename.grid(row=6,column=1)
entry_filename.insert(0,"chart.png") # Example input

# Create a button to submit the user input
button_submit = tk.Button(frame_input,text="Create Chart",command=get_input)
button_submit.grid(row=7,columnspan=2,pady=10)

# Create a label to display any errors
label_error=tk.Label(root,text="",fg="red")
label_error.pack()

# Start the main loop of the GUI
root.mainloop()
