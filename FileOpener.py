import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    # Create a Tkinter root window (hidden)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open file dialog
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*"))
    )
    
    return file_path