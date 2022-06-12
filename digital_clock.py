from tkinter import Label, Tk
import time

# set fram
root = Tk()
root.title("Digital Clock")
root.geometry("655x200")
root.resizable(1, 1)

# GUI, color, font,  border
text_font = ("Boulder colorado", 68, 'bold')
background = "#A3CEF1"  # A3CEF1 #6096BA
foreground = "#274C77"  # 8B8C89 #274C77
border_width = 50

# labels_widget
label = Label(root, font=text_font, bg=background,
              fg=foreground, bd=border_width)
label.grid(row=0, column=1)


# function
def digital_clock():
    time_live = time.strftime("%H:%M:%S  %p")
    label.config(text=time_live)
    label.after(200, digital_clock)


digital_clock()
root.mainloop()
