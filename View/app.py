import tkinter as tk
from tkinter import messagebox


class Window:
    def __init__(self, root):
        """Initialize the Tkinter window for GUI"""
        self.root = root
        self.root.title("Cow Milk Production System")

        self.main_frame = tk.Frame(root, padx=20, pady=20)
        self.main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.label_frame = tk.Frame(self.main_frame)
        self.label_frame.pack(pady=10)

        self.label = tk.Label(
            self.label_frame, text="Enter Cow ID (8-digit number):", font=("Arial", 14))
        self.label.pack(pady=5)

        self.cow_id_entry = tk.Entry(
            self.label_frame, font=("Arial", 14), width=25)
        self.cow_id_entry.pack(pady=5)

        self.submit_button = tk.Button(
            self.label_frame, text="Submit", font=("Arial", 14), command=self.submit_cow_id)
        self.submit_button.pack(pady=10)

        self.result_frame = tk.Frame(self.main_frame)
        self.result_frame.pack(pady=10)

        self.result_label = tk.Label(
            self.result_frame, text="Milk Production Results:", font=("Arial", 14))
        self.result_label.pack(pady=5)

        self.result_text = tk.Text(
            self.result_frame, height=10, width=60, font=("Arial", 12), wrap=tk.WORD)
        self.result_text.pack(pady=10)

        self.result_text.config(state=tk.DISABLED)

    def set_controller(self, controller):
        """Set the controller for handling logic and interaction with model"""
        self.controller = controller

    def submit_cow_id(self):
        """Validates and submits the cow ID"""
        cow_id = self.cow_id_entry.get().strip()
        if not cow_id.isdigit() or len(cow_id) != 8 or cow_id[0] == '0':
            self.display_message(
                "Invalid Cow ID! Please enter an 8-digit number, where the first digit is not 0.")
            return
        self.controller.submit_cow_id(cow_id)

    def display_message(self, message):
        """Displays a message in the result text area."""
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, message)
        self.result_text.config(state=tk.DISABLED)
