import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Import ttk for Treeview widget
import invoice_backend  # Importing the backend functions

# Set up the main application window
window = tk.Tk()
window.title("Invoice Manager")

# Entry fields for customer and invoice data
customer_name_label = tk.Label(window, text="Customer Name")
customer_name_label.grid(row=0, column=0)

customer_name_entry = tk.Entry(window)
customer_name_entry.grid(row=0, column=1)

item_name_label = tk.Label(window, text="Item Name")
item_name_label.grid(row=1, column=0)

item_name_entry = tk.Entry(window)
item_name_entry.grid(row=1, column=1)

price_label = tk.Label(window, text="Price")
price_label.grid(row=2, column=0)

price_entry = tk.Entry(window)
price_entry.grid(row=2, column=1)

quantity_label = tk.Label(window, text="Quantity")
quantity_label.grid(row=3, column=0)

quantity_entry = tk.Entry(window)
quantity_entry.grid(row=3, column=1)

# Function to add invoice to the database
def add_command():
    customer_name = customer_name_entry.get()
    item_name = item_name_entry.get()
    price_str = price_entry.get()
    quantity_str = quantity_entry.get()

    # Validate inputs
    if not customer_name or not item_name:
        messagebox.showerror("Input Error", "Customer Name and Item Name cannot be empty.")
        return
    
    try:
        price = float(price_str)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid price.")
        return
    
    try:
        quantity = int(quantity_str)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid quantity.")
        return

    total = price * quantity

    # Insert the new invoice into the database
    invoice_backend.insert(customer_name, item_name, price, quantity, total)

    # Clear the input fields
    customer_name_entry.delete(0, tk.END)
    item_name_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

    # Refresh the invoices list
    view_invoices()

# Function to view all invoices
def view_invoices():
    invoices = invoice_backend.view()  # Get all invoices
    for row in invoice_listbox.get_children():
        invoice_listbox.delete(row)
    for invoice in invoices:
        invoice_listbox.insert("", "end", values=invoice)

# Function to delete selected invoice
def delete_invoice():
    selected_item = invoice_listbox.selection()
    if not selected_item:
        messagebox.showerror("Selection Error", "Please select an invoice to delete.")
        return
    invoice_id = invoice_listbox.item(selected_item)["values"][0]
    invoice_backend.delete(invoice_id)
    view_invoices()

# Set up buttons
add_button = tk.Button(window, text="Add Invoice", width=15, command=add_command)
add_button.grid(row=4, column=0, columnspan=2)

view_button = tk.Button(window, text="View All Invoices", width=15, command=view_invoices)
view_button.grid(row=5, column=0, columnspan=2)

delete_button = tk.Button(window, text="Delete Invoice", width=15, command=delete_invoice)
delete_button.grid(row=6, column=0, columnspan=2)

# Set up the Listbox to display invoices
invoice_listbox = ttk.Treeview(window, columns=("ID", "Customer", "Item", "Price", "Quantity", "Total"), show="headings")
invoice_listbox.grid(row=7, column=0, columnspan=2)

invoice_listbox.heading("ID", text="ID")
invoice_listbox.heading("Customer", text="Customer")
invoice_listbox.heading("Item", text="Item")
invoice_listbox.heading("Price", text="Price")
invoice_listbox.heading("Quantity", text="Quantity")
invoice_listbox.heading("Total", text="Total")

# Start the application
window.mainloop()
