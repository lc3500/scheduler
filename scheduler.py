import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry("400x400")
root.title("Scheduling App")


# Create a PhotoImage object with your image file
bg_image = tk.PhotoImage(file="/Users/lwcrowder/Downloads/blob-scene-haikei.png")

# Create a label with the image as its background
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Create a notebook widget to hold the tasks
notebook = ttk.Notebook(root)
notebook.pack(pady=10)

# Create a function to save a task
def save_task():
    # Get the values from the entry fields
    date = date_entry.get()
    time = time_entry.get()
    task = task_entry.get()

    # Clear the entry fields
    date_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    task_entry.delete(0, tk.END)

    # Create a new tab for the task
    task_tab = ttk.Frame(notebook)
    notebook.add(task_tab, text=task)

    # Add the task details to the tab
    date_label = tk.Label(task_tab, text="Date: " + date, font=("Helvetica", 12))
    date_label.pack()
    time_label = tk.Label(task_tab, text="Time: " + time, font=("Helvetica", 12))
    time_label.pack()
    details_label = tk.Label(task_tab, text="Details:", font=("Helvetica", 12))
    details_label.pack()
    details_text = tk.Text(task_tab, height=10, width=50)
    details_text.pack(pady=10)

    # Save the task details to the tab
    details_text.insert(tk.END, task)

# Create a label for the title
title_label = tk.Label(root, text="Schedule", font=("Helvetica", 16))
title_label.pack()

# Create a label for the date
date_label = tk.Label(root, text="Date:", font=("Helvetica", 12))
date_label.pack()

# Create an entry field for the date
date_entry = tk.Entry(root, font=("Helvetica", 12))
date_entry.pack()

# Create a label for the time
time_label = tk.Label(root, text="Time:", font=("Helvetica", 12))
time_label.pack()

# Create an entry field for the time
time_entry = tk.Entry(root, font=("Helvetica", 12))
time_entry.pack()

# Create a label for the task
task_label = tk.Label(root, text="Task:", font=("Helvetica", 12))
task_label.pack()

# Create an entry field for the task
task_entry = tk.Entry(root, font=("Helvetica", 12))
task_entry.pack()

# Create a button to save the task
save_button = tk.Button(root, text="Save", font=("Helvetica", 12), command=save_task)
save_button.pack(pady=20)

# Run the main loop
root.mainloop()
