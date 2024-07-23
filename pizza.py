import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def place_order():
    pizza_type = pizza_var.get()
    quantity = quantity_var.get()
    size = size_var.get()

    if not quantity.isdigit():
        messagebox.showerror("Error", "Quantity must be a number.")
        return

    order_message = f"You ordered {quantity} {pizza_type} {size} size pizza(s)."
    messagebox.showinfo("Order Confirmation", order_message)

root = tk.Tk()
root.title("Pizza App")

# Title
title_label = tk.Label(root, text="Welcome to Pizza Hut", font=("Arial", 16))
title_label.pack(pady=10)

# Pizza type selection
pizza_var = tk.StringVar(root)
pizza_var.set("Veg Extravaganza")  # Default value
pizza_label = tk.Label(root, text="Select Your Fav Pizza:")
pizza_label.pack()
pizza_options = ["Veg Extravaganza", "Non-Veg Supreme", "Pepperoni"]
pizza_dropdown = ttk.Combobox(root, textvariable=pizza_var, values=pizza_options)
pizza_dropdown.pack()

# Quantity input
quantity_label = tk.Label(root, text="Enter Quantity:")
quantity_label.pack()
quantity_var = tk.StringVar(root)
quantity_entry = tk.Entry(root, textvariable=quantity_var)
quantity_entry.pack()

# Size selection
size_label = tk.Label(root, text="Select Size:")
size_label.pack()
size_var = tk.StringVar(root)
size_var.set("S")  # Default value
size_options = ["S", "M", "L"]
for size in size_options:
    size_radio = tk.Radiobutton(root, text=size, variable=size_var, value=size)
    size_radio.pack()

# Order button
order_button = tk.Button(root, text="Order", command=place_order)
order_button.pack(pady=10)

root.mainloop()