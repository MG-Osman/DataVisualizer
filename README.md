# Custom Data Visualization

This is a Python program that uses matplotlib to create custom data visualizations based on the user input. The program asks the user to enter the data for the x and y values, the type of chart they want to create (line, bar, scatter, hist or pie), and the labels and title for the chart. The program also asks the user to enter a file name to save the chart as an image file. The program then uses the create_chart() function to plot the data and show the chart on the screen. The program handles any errors or invalid inputs from the user.

## Requirements

To run this program, you will need:

- Python 3.x
- matplotlib
- numpy
- ast
- tkinter

## Usage

To run this program, you can use any IDE or editor that supports Python, or run it from the command line. When you run the program, you will see a GUI window with the input widgets and a button to create the chart like this one:
![GUIwindow](https://user-images.githubusercontent.com/58115228/235950594-0d913cae-0e70-4401-921f-1f8aab170738.png)

Enter your data and preferences in the corresponding fields and click on the button. You will see your custom chart on the screen and also saved as an image file in your directory.

Here are some examples of charts that you can create with this program:

## Code Explanation

The code consists of two main parts: a function to create a custom chart and a GUI to get the user input.

The create_chart() function takes six parameters: x, y, kind, xlabel, ylabel, title, and filename. The x and y parameters are lists or arrays of data values for the x and y axes. The kind parameter is a string that specifies the type of chart to create (line, bar, scatter, hist or pie). The xlabel and ylabel parameters are strings that specify the labels for the x and y axes. The title parameter is a string that specifies the title for the chart. The filename parameter is a string that specifies the file name to save the chart as an image file.

The function creates a figure and an axis object using plt.subplots(). Then it checks the kind parameter and plots the data accordingly using different methods from matplotlib. For example, if kind is "line", it uses ax.plot(data) to create a line chart. It also sets the title and labels for the axis using ax.set_title(), ax.set_xlabel(), and ax.set_ylabel(). If kind is "pie", it also adds a legend using ax.legend(). Finally, it saves the figure as an image file using fig.savefig() and shows it on the screen using plt.show().

The GUI part uses tkinter to create a root window and a frame to hold the input widgets. It creates labels and entries for each parameter of the create_chart() function using tk.Label() and tk.Entry(). It also inserts some example inputs in each entry using entry.insert(). It creates a button to submit the user input using tk.Button() and assigns it a command to call a function called get_input(). It also creates a label to display any errors using tk.Label().

The get_input() function tries to get the user input from each entry using entry.get() and convert it to the appropriate data type using ast.literal_eval(). If there is any exception, it displays it in the error label using label_error.config(). Otherwise, it clears the error label and calls the create_chart() function with the user input.

## Future Improvements

This program is a simple demonstration of how to create custom data visualizations using matplotlib and tkinter. There are many ways to improve it and add more features. For example, you can:

- Add more options for the user to customize the chart elements, such as color, size, style, etc.
- Add more types of charts that matplotlib supports, such as boxplot, contour, heatmap, etc.
- Add validation and error handling for the user input, such as checking if the data is valid, if the file name is unique, etc.
- Add a file browser or a drag-and-drop feature for the user to select the file name and location to save the chart.
- Add a preview feature for the user to see the chart before saving it.
- Add a help or tutorial feature for the user to learn how to use the program and enter the data correctly.
