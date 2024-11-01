import tkinter as tk

# Function to calculate volume of a box (Length * Width * Height)
def calculate_volume():
    # Get values from the entry boxes and convert to integers
    length = int(length_entry.get())
    width = int(width_entry.get())
    height = int(height_entry.get())
    
    # Calculate volume
    volume = length * width * height
    
    # Show the result in result_label
    result_label.config(text=f"Volume: {volume} cubic units")

# Set up the main window
root = tk.Tk()
root.title("Simple Volume Calculator")

# Labels and entry boxes for length, width, and height
tk.Label(root, text="Enter Length:").grid(row=0, column=0)
tk.Label(root, text="Enter Width:").grid(row=1, column=0)
tk.Label(root, text="Enter Height:").grid(row=2, column=0)

# Entry fields for length, width, and height
length_entry = tk.Entry(root)
width_entry = tk.Entry(root)
height_entry = tk.Entry(root)

# Arrange entry fields in the window
length_entry.grid(row=0, column=1)
width_entry.grid(row=1, column=1)
height_entry.grid(row=2, column=1)

# Button to calculate and display the volume
tk.Button(root, text="Calculate Volume", command=calculate_volume).grid(row=3, column=1)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=1)

# Run the main loop
root.mainloop()
