import tkinter as tk
import random

window = tk.Tk()
# Tentry = tk.Entry()
window.geometry("300x300")
label = tk.Label(
    text="Timer Calculator",
    foreground="white",  # Set the text color to white
    background="black",  # Set the background color to black
    width=100,
    height=2
)
entry = tk.Entry()

frame = tk.Frame(
    height=10
)


def send_message():
    var = entry.get()
    print(var)
    result_1.config(
        text=var
    )


button = tk.Button(
    text="Click me!",
    bg="blue",
    fg="yellow",
    width=10,
    height=1,
    command=send_message
)

result = tk.Label(
    text="0.0",
    foreground="red",  # Set the text color to white
    font=("Arial", 25)
)

frame_2 = tk.Frame(
    height=10
)

result_1 = tk.Label(
    foreground="green",  # Set the text color to white
    font=("Arial", 25)
)

for c in window.children:
    print(c)
    window.children[c].pack()


def timer_update():
    value = random.randint(1, 9), random.randint(1, 9)
    result.config(text=value)
    window.after(2000, timer_update)


window.after(2000, timer_update)

window.mainloop()