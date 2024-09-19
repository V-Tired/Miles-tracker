import datetime as dt
from miles import miles
from tkinter import *
import os

"""A GUI application to keep track of miles driven to 5 different locations in a csv."""

# Colors and Fonts
LIGHT = "#FFE6E6"
PINK = "#E1AFD1"
MID = "#AD88C6"
DARK = "#7469B6"
GREY = "#4c545c"
FONT = ("georgia", 12, "bold")


class Tracker:
    """Handles all the buttons and file management for the mile tracker."""
    def __init__(self):
        self.miles = miles
        self.date = Entry
        self.note = Entry
        today = dt.datetime.today()
        self.today = f"{today.month}/{today.day}/{today.year}"
        header = Label(
            text="Mileage Tracker",
            font=FONT,
            bg=GREY,
            fg=LIGHT
        )
        header.grid(column=0, row=0, columnspan=6, pady=20)
        if not os.path.exists("miles.csv"):
            with open("miles.csv", mode='w') as file:
                file.write("")
        with open("miles.csv", mode='r') as file:
            content = file.readlines()
        self.csv = content
        self.display()

    def enter_date(self, column, name):
        """Create entry form for date, autofill with today's date"""
        self.date = Entry(width=8)
        self.date.insert(0, self.today)
        self.date.grid(column=column, row=3, pady=5, padx=2)
        self.note = Entry(width=15)
        self.note.grid(column=column, row=4, pady=5, padx=2)

        submit = Button(text="Submit", font=("georgia", 8, "bold"), bg=DARK, fg=PINK,
                        command=lambda: self.add_entry(name))
        submit.grid(column=column, row=5, )

    def display(self):
        """Displays all buttons for different locations"""
        wayne = Button(text="Wayne", font=FONT, bg=DARK, fg=PINK, command=lambda column=0,
                       name="Wayne": self.enter_date(column, name),)
        wayne.grid(column=0, row=1, padx=2)
        main_line = Button(text="Main Line", font=FONT, bg=DARK, fg=PINK,
                           command=lambda column=1, name="Main Line": self.enter_date(column, name),)
        main_line.grid(column=1, row=1, padx=2)
        hattie = Button(text="HWS", font=FONT, bg=DARK, fg=PINK,
                        command=lambda column=2, name="HWS": self.enter_date(column, name),)
        hattie.grid(column=2, row=1, padx=2)
        del_art = Button(text="DAM", font=FONT, bg=DARK, fg=PINK,
                         command=lambda column=3, name="DAM": self.enter_date(column, name),)
        del_art.grid(column=3, row=1, padx=2)
        tls = Button(text="TLS", font=FONT, bg=DARK, fg=PINK,
                     command=lambda column=4, name="TLS": self.enter_date(column, name),)
        tls.grid(column=4, row=1, padx=2)

    def add_entry(self, name):
        """Adds entries to the csv"""
        date = self.date.get()
        note = self.note.get()
        self.date.delete(first=0, last="end")
        self.note.delete(first=0, last="end")
        name = name
        miles_to_add = self.miles[name]
        with open("miles.csv", mode='a') as file:
            file.write(f"{name}, {date}, {note}, {miles_to_add}\n")


# Window Config
window = Tk()
window.minsize(200, 200)
window.config(bg=GREY, padx=20, pady=20)


tracker = Tracker()
window.mainloop()
