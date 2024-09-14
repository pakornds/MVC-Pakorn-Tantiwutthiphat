import tkinter as tk
from Model.cow_milk_model import CowMilkModel
from Controller.cow_milk_controller import CowMilkController
from View.app import Window

#
if __name__ == "__main__":
    """"The main part of the program that initializes the MVC components and runs the GUI application"""
    layout = tk.Tk()

    model = CowMilkModel()

    view = Window(layout)

    controller = CowMilkController(view, model)

    layout.mainloop()
