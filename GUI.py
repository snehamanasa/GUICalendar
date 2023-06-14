from tkinter import *
from PIL import ImageTk, Image
import calendar
import datetime


def show_calendar():
    year = entry.get()

    if not year.isdigit():
        l1.config(text="Invalid year! Please enter a valid year.")
        return

    year = int(year)

    if year < 1500 or year > 9999:
        l1.config(text="Invalid year! Please enter a valid year.")
        return

    text = calendar.calendar(year)
    l1.config(text=text)


root = Tk()
root.title("GUI CALENDAR BY PYTHON")
root.config(background="white")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the maximum font size based on the screen size
max_font_size = min(screen_width, screen_height) // 40

frame = Frame(root, bg="white")
frame.grid(row=1, column=0, padx=10, pady=10, sticky="NW")

label1 = Label(frame, text="WELCOME TO MY CALENDAR", bg='white', font=("Colfox", max_font_size-2, 'bold'))
label1.grid(row=3, column=0, padx=10, pady=10, sticky="W")

label2 = Label(frame, text="Enter the Year", bg='white', font=("Colfox", max_font_size-4))
label2.grid(row=4, column=0, padx=10, pady=10, sticky="W")

entry = Entry(frame, font=("Colfox", max_font_size-6))
entry.grid(row=5, column=0, padx=10, pady=10, sticky="W")

button = Button(frame, text="Show Calendar",bg='seashell', font=("Colfox", max_font_size-4), command=show_calendar)
button.grid(row=6, column=0, padx=10, pady=10, sticky="W")

l1 = Label(root, font=("consolas", max_font_size-8, 'bold'), justify="left", bg='seashell')
l1.grid(row=0, column=1, rowspan=4, padx=10, pady=10, sticky="NSEW")

# Get the current year
current_year = datetime.date.today().year

# Show the calendar for the current year
text = calendar.calendar(current_year)
l1.config(text=text)

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(3, weight=1)

# Increase the size of l1
l1.grid_rowconfigure(0, weight=1)

root.mainloop()
