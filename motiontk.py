import tkinter as tk

# Function to calculate speed and determine if the character reaches the destination
def calculate_speed():
    distance = distance_entry.get()  # Get distance input
    time = time_entry.get()  # Get time input

    # Check if the distance and time inputs are not empty and are numeric
    if distance and time:  # Check if inputs are not empty
        if distance.isnumeric() and time.isnumeric():  # Check if inputs are numeric
            distance = float(distance)  # Convert to float
            time = float(time)  # Convert to float
            
            # Validate time to avoid division by zero
            if time > 0:
                speed = distance / time  # Calculate speed
                result_label.config(text=f"Speed: {speed:.2f} m/s")  # Display speed
                
                # Game condition: check if speed is sufficient to reach the destination
                if speed >= 10:  # Assuming 10 m/s is the required speed to reach
                    outcome_label.config(text="Congratulations! You reached your destination!")
                else:
                    outcome_label.config(text="Oh no! You need to go faster to reach your destination.")
            else:
                result_label.config(text="Time must be greater than zero.")
        else:
            result_label.config(text="Please enter valid numbers for distance and time.")
    else:
        result_label.config(text="Please fill in both fields.")

# Set up the main application window
root = tk.Tk()
root.title("Speed Challenge Game")

# Create and place widgets
welcome_label = tk.Label(root, text="Welcome to the Speed Challenge Game!", font=("Arial", 16))
welcome_label.pack(pady=10)

distance_label = tk.Label(root, text="Enter Distance to Travel (meters):")
distance_label.pack(pady=10)

distance_entry = tk.Entry(root)
distance_entry.pack(pady=5)

time_label = tk.Label(root, text="Enter Time to Reach (seconds):")
time_label.pack(pady=10)

time_entry = tk.Entry(root)
time_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate Speed", command=calculate_speed)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

outcome_label = tk.Label(root, text="", font=("Arial", 14))
outcome_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
