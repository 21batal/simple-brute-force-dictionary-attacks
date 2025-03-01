#!/usr/bin/env python
# coding: utf-8

# In[10]:


import tkinter as tk
from tkinter import messagebox, ttk
import itertools
import string

# Hardcoded correct password
CORRECT_PASSWORD = "anita"

# Read the dictionary file
def load_dictionary(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]

# Load the dictionary from the file
DICTIONARY = load_dictionary("UserPassCombo-Jay.txt")

def dictionary_attack(username):
    attempts = 0
    for password in DICTIONARY:
        attempts += 1
        if password == CORRECT_PASSWORD:
            return True, attempts, password
    return False, attempts, None

def brute_force_attack():
    chars = string.ascii_letters  # A-Z, a-z
    attempts = 0
    for length in range(1, 6):  # Up to 5 characters
        for attempt in itertools.product(chars, repeat=length):
            attempts += 1
            if ''.join(attempt) == CORRECT_PASSWORD:
                return True, attempts, ''.join(attempt)
    return False, attempts, None

def on_submit():
    username = entry_username.get()
    success, attempts, password = dictionary_attack(username)
    if success:
        messagebox.showinfo("Success", f"Dictionary Attack Successful!\nAttempts: {attempts}\nPassword: {password}")
    else:
        success, attempts, password = brute_force_attack()
        if success:
            messagebox.showinfo("Success", f"Brute Force Attack Successful!\nAttempts: {attempts}\nPassword: {password}")
        else:
            messagebox.showinfo("Failure", f"Both attacks failed.\nTotal Attempts: {attempts}")

# GUI setup
root = tk.Tk()
root.title("Password Cracker")
root.geometry("500x400")  # Set window size
root.configure(bg="#F5F5F5")  # Light gray background

# Custom font
custom_font = ("Helvetica", 12)
title_font = ("Helvetica", 20, "bold")

# Frame for better organization
frame = tk.Frame(root, bg="#FFFFFF", padx=30, pady=30, bd=2, relief="flat")
frame.pack(pady=40, padx=40, fill="both", expand=True)

# Title label
title_label = tk.Label(frame, text="Password Cracker", font=title_font, bg="#FFFFFF", fg="#2C3E50")
title_label.pack(pady=20)

# Username label and entry
label_username = tk.Label(frame, text="Enter Username:", font=custom_font, bg="#FFFFFF", fg="#34495E")
label_username.pack(pady=5)

entry_username = tk.Entry(frame, font=custom_font, bg="#ECF0F1", fg="#2C3E50", insertbackground="#2C3E50", bd=2, relief="flat")
entry_username.pack(pady=10, ipady=5, ipadx=10)

# Submit button with styling
submit_button = ttk.Button(frame, text="Submit", command=on_submit, style="TButton")
submit_button.pack(pady=20)

# Style for the button
style = ttk.Style()
style.configure("TButton", font=custom_font, background="#3498DB", foreground="#FFFFFF", padding=10, borderwidth=0)
style.map("TButton", background=[("active", "#2980B9")])  # Darker blue on hover

# Footer label
footer_label = tk.Label(root, text="© 2023 Password Cracker", font=("Helvetica", 10), bg="#F5F5F5", fg="#7F8C8D")
footer_label.pack(side="bottom", pady=10)

root.mainloop()


# In[ ]:





# In[ ]:




