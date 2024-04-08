# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import tkinter as tk
from tkinter import filedialog, messagebox
from steganography.steganography import Steganography
import os
import binascii

def to_hex(s):
    """
    Convert string to hexadecimal.
    """
    return binascii.hexlify(s.encode()).decode()

def from_hex(h):
    """
    Convert hexadecimal to string.
    """
    return binascii.unhexlify(h).decode()

# Function for hiding text
def hide_text():
    # Display "Please wait" message
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "Please wait...")

    carrier_path = carrier_entry.get()
    secret_text = text_entry.get("1.0", tk.END).strip()  # Strip trailing newline
    output_path = "stego.png"
    
    try:
        Steganography.encode(carrier_path, output_path, secret_text)
        messagebox.showinfo("Success", "Text successfully hidden!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

    # Reset result display
    result_text.delete("1.0", tk.END)
    result_text.config(state=tk.DISABLED)

# Function for finding hidden text
def find_text():
    steg_img = steg_img_entry.get()
    try:
        secret_text = Steganography.decode(steg_img)
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Hidden text found: " + secret_text)
        result_text.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create main window
root = tk.Tk()
root.title("Steganography Tool")

# Function to get user's home directory
def get_home_directory():
    home = os.path.expanduser("~")
    return home

# Carrier file entry
carrier_label = tk.Label(root, text="Carrier File:")
carrier_label.grid(row=0, column=0, sticky="e")
carrier_entry = tk.Entry(root, width=50)
carrier_entry.grid(row=0, column=1, padx=5, pady=5)
carrier_button = tk.Button(root, text="Browse", command=lambda: carrier_entry.insert(tk.END, filedialog.askopenfilename(initialdir=get_home_directory() + "/Downloads")))
carrier_button.grid(row=0, column=2, padx=5, pady=5)

# Text to hide entry
text_label = tk.Label(root, text="Text to Hide:")
text_label.grid(row=1, column=0, sticky="e")
text_entry = tk.Text(root, width=50, height=5)
text_entry.grid(row=1, column=1, padx=5, pady=5)

# Button to hide text
hide_button = tk.Button(root, text="Hide Text", command=hide_text)
hide_button.grid(row=2, column=1, padx=5, pady=5)

# Image with hidden text entry
steg_img_label = tk.Label(root, text="Image with Hidden Text:")
steg_img_label.grid(row=3, column=0, sticky="e")
steg_img_entry = tk.Entry(root, width=50)
steg_img_entry.grid(row=3, column=1, padx=5, pady=5)
steg_img_button = tk.Button(root, text="Browse", command=lambda: steg_img_entry.insert(tk.END, filedialog.askopenfilename(initialdir=get_home_directory() + "/Pictures")))
steg_img_button.grid(row=3, column=2, padx=5, pady=5)

# Button to find hidden text
find_button = tk.Button(root, text="Find Hidden Text", command=find_text)
find_button.grid(row=4, column=1, padx=5, pady=5)

# Result display
result_text = tk.Text(root, width=50, height=5, state=tk.DISABLED)
result_text.grid(row=5, column=1, padx=5, pady=5)

root.mainloop()
