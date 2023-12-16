from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import os


# creates a window
root = tk.Tk()
root.title("Simple Budget Organizer!")

# creates a notebook
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# create a frame
frame1 = ttk.Frame(notebook, width=400, height=280)


# add frame to notebook
notebook.add(frame1, text='Current Paycheck')


# Global variable to store net income
net_income = 0

# Function to add an expense
def add_expense():
    global net_income

    # Retrieve data from entry widgets
    expense_type = typeexpense_entry.get()
    expense_amount = amount_entry.get()

    # Validate and process data
    try:
        expense_amount = float(expense_amount)  # Convert amount to a float
        if expense_type and expense_amount > 0 and expense_amount <= net_income:
            # Calculate the remaining income
            net_income -= expense_amount
            remaining_income_label.config(text=f"Remaining Income: ${net_income}")

            # Add data to treeview with a tag for color
            item_id = expenses_tree.insert('', 'end', values=(expense_type, expense_amount, net_income))
            expenses_tree.item(item_id, tags=('expense_amount',))
            
            # Clear the entries for new data
            typeexpense_entry.delete(0, 'end')
            amount_entry.delete(0, 'end')
        else:
            print("Invalid input or expense exceeds remaining income")
    except ValueError:
        print("Invalid amount")

# Function to confirm and set net income
def confirm_and_set_net_income():
    global net_income
    response = messagebox.askyesno("Confirm Reset", "Setting a new income will remove your current progress. Are you sure you want to proceed?")
    if response:
        try:
            net_income = float(netincome_entry.get())
            remaining_income_label.config(text=f"Remaining Income: ${net_income}")
            # Clear the treeview table
            for item in expenses_tree.get_children():
                expenses_tree.delete(item)
        except ValueError:
            print("Invalid income amount")

## function to close windown
def close():
    frame1.destroy()

# creates labels and entries for expenses in frame1
netincome = ttk.Label(frame1, text="Enter your net income:", background="", foreground="black", font=("Helvetica", 14))
netincome.pack(anchor='w')

netincome_entry = ttk.Entry(frame1)
netincome_entry.pack(anchor='w')

netincome_button = ttk.Button(frame1, text="Set Net Income", command=confirm_and_set_net_income)
netincome_button.pack(anchor='w')

typeexpense = ttk.Label(frame1, text="Type of expense:", background="", foreground="black", font=("Helvetica", 14))
typeexpense.pack(anchor='w')

typeexpense_entry = ttk.Entry(frame1)
typeexpense_entry.pack(anchor='w')

amount = ttk.Label(frame1, text="Amount: $", background="", foreground="black", font=("Helvetica", 14))
amount.pack(anchor='w')

amount_entry = ttk.Entry(frame1)
amount_entry.pack(anchor='w')

# creates treeview table for the expenses
columns = ("Type of expense", "Amount", "Remaining")
expenses_tree = ttk.Treeview(frame1, columns=columns, show="headings")
for col in columns:
    expenses_tree.heading(col, text=col)
expenses_tree.pack(anchor='w')

# Configure the tag for expense amount color
expenses_tree.tag_configure('expense_amount', foreground='red')

# Label to display remaining income
remaining_income_label = ttk.Label(frame1, text="Remaining Income: $")
remaining_income_label.pack(anchor='e')

# add expense button
add_button = ttk.Button(frame1, text="Add Expense", command=add_expense)
add_button.pack(anchor='w')

# add exit button to close window 
exit_button = ttk.Button(frame1, text="EXIT", command=close)
exit_button.pack(anchor='e')


# Load the images (had to create paths to my images as the system was not recognizing any other way.)
base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'budget.png')
photo = PhotoImage(file=image_path)

## Creates the label to place image in the window
image_label = tk.Label(frame1, image = photo)
image_label.place(x=250, y=0) 


root.mainloop()
