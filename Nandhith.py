import random
import tkinter as tk

# 5 days, 7 periods per day
matrix = [[0, 0, 0, 0, 0, 0, 0] for _ in range(5)]

# Total theory and lab sessions per week
class_schedule = {
    "Math_Lab": 1,
    "Python_Lab": 1,
    "Python_Theory": 2,
    "Material_Science_Lab": 1,
    "Material_Science_Theory": 2,
    "Design_Lab": 1,
    "Design_Theory": 2,
    "Actuators_Drives_Theory": 3,
    "Mechanisms&Machines_Lab": 1,
    "Mechanisms&Machines_Theory": 3,
    "Microcontrollers_Lab": 1,
    "Microcontrollers_Theory": 3,
    "LSE": 3,
    "Mahabharata":1,
    "Math": 3,
    "Library":1
}

lablist = ["Python_Lab", "Material_Science_Lab", "Design_Lab", "Mechanisms&Machines_Lab", "Microcontrollers_Lab","Math_Lab"]

# Randomly assign classes to periods while tracking counts
for j in range(5):  # For each day
    i = 0
    while i < 7:  # For each period in a day
        # Filter out classes with no remaining sessions
        available_classes = [cls for cls, count in class_schedule.items() if count > 0]
        
        if not available_classes:
            break  # Stop if there are no more classes to schedule
        
        choice = random.choice(available_classes)  # Choose a random class
        
        if choice in lablist:
            if i == 0 and i + 2 < 7:  # Labs can only be placed in first, fourth, or sixth periods
                matrix[j][i] = matrix[j][i+1] = matrix[j][i+2] = choice
                class_schedule[choice] -= 1  # Reduce count after scheduling
                i += 3
            elif i == 3 and i + 1 < 7:
                matrix[j][i] = matrix[j][i+1] = choice
                class_schedule[choice] -= 1
                i += 2
            elif i == 5 and i + 1 < 7:
                matrix[j][i] = matrix[j][i+1] = choice
                class_schedule[choice] -= 1
                i += 2
            else:
                continue
        else:
            matrix[j][i] = choice  # Place theory class
            class_schedule[choice] -= 1
            i += 1

# Color dictionary for each class
color_dict = {
    "Python_Lab": "lightblue",
    "Python_Theory": "blue",
    "Material_Science_Lab": "lightgreen",
    "Material_Science_Theory": "green",
    "Design_Lab": "lightpink",
    "Design_Theory": "pink",
    "Actuators_Drives_Theory": "yellow",
    "Mechanisms&Machines_Lab": "lightgray",
    "Mechanisms&Machines_Theory": "gray",
    "Microcontrollers_Lab": "lightcoral",
    "Microcontrollers_Theory": "coral",
    "LSE": "orange",
    "Mahabharata": "purple",
    "Math": "brown",
    "Math_lab": "lightblue"
}

# Create a Tkinter window
root = tk.Tk()
root.title("Timetable")

# Days and periods headers
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
periods = ["1", "2", "3", "4", "5", "6", "7"]

# Create headers for days and periods
for i, day in enumerate(days):
    label = tk.Label(root, text=day, relief=tk.RAISED)
    label.grid(row=i+1, column=0, sticky="nsew")

for i, period in enumerate(periods):
    label = tk.Label(root, text=period, relief=tk.RAISED)
    label.grid(row=0, column=i+1, sticky="nsew")

# Keep track of already spanned cells
spanned_cells = set()

# Fill in the timetable with the classes and colors
for i in range(5):  # Days
    j = 0  # Periods
    while j < 7:
        subject = matrix[i][j]
        
        if subject == 0:
            label = tk.Label(root, text="", relief=tk.RAISED, width=12, height=4)
            label.grid(row=i+1, column=j+1, sticky="nsew")
            j += 1  # Move to the next period
        elif (i, j) not in spanned_cells:  # Check if this cell is part of a previously spanned cell
            color = color_dict.get(subject, "white")  # Default to white if not found in color_dict
            
            # Check if the subject spans multiple periods (i.e., lab)
            if j+2 < 7 and matrix[i][j] == matrix[i][j+1] == matrix[i][j+2]:  # Lab spanning 3 periods
                label = tk.Label(root, text=subject, bg=color, relief=tk.RAISED, width=36, height=4)
                label.grid(row=i+1, column=j+1, columnspan=3, sticky="nsew")
                spanned_cells.update([(i, j), (i, j+1), (i, j+2)])  # Mark these cells as spanned
                j += 3  # Move forward by 3 periods
            elif j+1 < 7 and matrix[i][j] == matrix[i][j+1]:  # Lab spanning 2 periods
                label = tk.Label(root, text=subject, bg=color, relief=tk.RAISED, width=24, height=4)
                label.grid(row=i+1, column=j+1, columnspan=2, sticky="nsew")
                spanned_cells.update([(i, j), (i, j+1)])  # Mark these cells as spanned
                j += 2  # Move forward by 2 periods
            else:  # Single period class (theory)
                label = tk.Label(root, text=subject, bg=color, relief=tk.RAISED, width=12, height=4)
                label.grid(row=i+1, column=j+1, sticky="nsew")
                j += 1  # Move to the next period

# Run the application
root.mainloop()
