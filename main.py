import tkinter as tk
from Model.cow_milk_model import CowMilkModel  # Importing the model
# Importing the controller
from Controller.cow_milk_controller import CowMilkController
from View.app import Window  # Importing the view

# The main part of the program that initializes the MVC components and runs the GUI application
if __name__ == "__main__":
    layout = tk.Tk()  # Create the root window for the GUI

    model = CowMilkModel()  # Create the model (handles data and milk calculations)

    view = Window(layout)  # Create the view (handles the GUI)

    # Create the controller (connects the view and model)
    controller = CowMilkController(view, model)

    layout.mainloop()  # Start the GUI event loop
