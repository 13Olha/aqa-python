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