# Функція приймає аргументом список кольорів і повертає один з кольорів списку.
# Функція не може повертати один і той самий колір підряд

# Функція приймає два аргументи, першиим аргументом буде числове значення для нижньої границі рандомного відліку часу,
# другим аргументом буде числове значення для верхньої границі рандомного відліку часу.
# Функція повертає рандомне числове значення часу між нижньою і верхньою границею.

# Функція ініціалізації,яка буде відмальовувати вікно разом з графічними елементами в ньому:
# 1 опис того, що має зробити юзер,
# 2 кнопка
# 3 проміжок часу між тим коли загорівся червоний колір і коли юзер натиснув на кнопку
# 4 опис поля 3 з проміжком часу
# 5 повідомлення про кількість невірних натискань на кнопку якщо загорівся інший колір

# - Функція рахує відлік з моменту підсвічення кнопки до моменту натиснення на неї

# 1. Чи лічильник невірних натискань кнопки (не червоної) повинен обнулятися після натискання червоної кнопки?
# 2. Що повинно відбуватися з програмmою якщо юзер не активний довгий час?


# import tkinter as tk
# import random
#
# colors = ["red", "green", "yellow", "violet", "blue"]
# current_color = "red"
# label = None
# window = None
# button = None
#
#
# def set_random_color(colors_list):
#     global current_color
#     current_color = random.choice(colors_list)
#
#
# def get_random_time(start_time, end_time):
#     return random.randint(start_time, end_time)
#
#
# def onclick():
#     print(current_color)
#
#
# def init_ui():
#     global label
#     global window
#     global button
#     window = tk.Tk()
#     window.geometry("300x300")
#     label = tk.Label(
#         text="Color Clicker",
#         foreground="white",  # Set the text color to white
#         background="black",  # Set the background color to black
#         width=100,
#         height=2
#     )
#     button = tk.Button(
#         text="Click me!",
#         bg="blue",
#         fg="yellow",
#         width=10,
#         height=1,
#         command=onclick
#     )
#     for c in window.children:
#         window.children[c].pack()
#
#
# def update_label(text):
#     global label
#     label.config(text=text)
#
#
# init_ui()
# # users_text = input('Type here')
# # window.after(2000, update_label, users_text)
# window.mainloop()


import tkinter as tk
import random
import time


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Color Clicker App")
        self.geometry("300x300")

        self.colors = ["red", "green", "blue"]
        self.color_time_range = (2, 4)

        self.title_label = tk.Label(self, text="Click a button when I am red", font=("Arial", 16))
        self.title_label.pack()

        self.red_button = tk.Button(self, text="Click me when title is red", command=self.on_button_click)
        self.red_button.pack()

        self.result_label = tk.Label(self, text="", font=("Arial", 12))
        self.result_label.pack()

        self.false_click_label = tk.Label(self, text="", font=("Arial", 12))
        self.false_click_label.pack()

        self.start_time = None
        self.current_color = ""
        self.false_clicks = 0

        self.change_title_color_id = None

        self.change_title_color()

    def change_title_color(self):
        new_color = random.choice(self.colors)
        while new_color == self.current_color:
            new_color = random.choice(self.colors)
        self.current_color = new_color
        self.title_label.configure(fg=new_color)

        if new_color == "red":
            self.start_time = time.time()
        else:
            self.start_time = None

        sleep_time = random.randint(*self.color_time_range)
        self.change_title_color_id = self.after(sleep_time * 1000, self.change_title_color)

    def on_button_click(self):
        if self.start_time is not None:
            end_time = time.time()
            elapsed_time = end_time - self.start_time
            self.result_label.configure(text=f"Time to click button: {elapsed_time:.2f} seconds")
            self.after_cancel(self.change_title_color_id)
            self.change_title_color()
        else:
            self.false_clicks += 1
            self.false_click_label.configure(text=f"False clicks (when title isn't red): {self.false_clicks}")


if __name__ == "__main__":
    app = App()
    app.mainloop()