import tkinter as tk
from tkinter import Canvas
import random
from PIL import Image, ImageTk

class Turtle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 50
        self.y = 400
        self.speed = None
        self.sprite = None
        self.image_path = Image.open("images/turtle.png")
        self.resize_image = self.image_path.resize((102, 75), Image.Resampling.LANCZOS)
        self.image = ImageTk.PhotoImage(self.resize_image)

    def update_position(self):
        self.speed = random.randint(2,3)
        self.x += self.speed
        
    def draw(self):
        self.sprite = self.canvas.create_image(self.x, self.y, image=self.image)
        
class Hare:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 50
        self.y = 410
        self.speed = None
        self.sprite = None
        self.image_path = Image.open("images/hare.png")
        self.resize_image = self.image_path.resize((102, 91), Image.Resampling.LANCZOS)
        self.image = ImageTk.PhotoImage(self.resize_image)

    def update_position(self):
        behavior = random.randint(1, 10)
        if behavior <= 3:
            self.speed = 0
        elif behavior <= 7:
            self.speed = 3
        else:
            self.speed = random.randint(3,6)
        self.x += self.speed
        
    def draw(self):
        self.sprite = self.canvas.create_image(self.x, self.y, image=self.image)


class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.image_path = "images/th_bg.png"
        self.image = Image.open(self.image_path)
        self.original_image = Image.open(self.image_path)
        self.resized_image = self.original_image.resize((800, 500), Image.Resampling.LANCZOS)

        self.finish_image_path = "images/finish.png"
        self.finish_image = Image.open(self.finish_image_path)
        self.finish_resized_image = self.finish_image.resize((135, 216), Image.Resampling.LANCZOS)
        self.finish_bg_image = ImageTk.PhotoImage(self.finish_resized_image)
        self.bg_image = ImageTk.PhotoImage(self.resized_image)

        self.header_path = "images/header.png"
        self.header_image = Image.open(self.header_path)
        self.header_resized_image = self.header_image.resize((292, 144), Image.Resampling.LANCZOS)
        self.header_bg_image = ImageTk.PhotoImage(self.header_resized_image)

        self.start_button_path = "images/start_button.png"
        self.start_button_image = Image.open(self.start_button_path)
        self.start_button_resized_image = self.start_button_image.resize((149, 64   ), Image.Resampling.LANCZOS)
        self.start_button_bg_image = ImageTk.PhotoImage(self.start_button_resized_image)

        self.hare_wins_image_path = "images/hare_wins.png"
        self.hare_wins_image = Image.open(self.hare_wins_image_path)
        self.hare_wins_resized_image = self.hare_wins_image.resize((294, 95), Image.Resampling.LANCZOS)
        self.hare_wins_bg_image = ImageTk.PhotoImage(self.hare_wins_resized_image)

        self.turtle_wins_image_path = "images/turtle_wins.png"
        self.turtle_wins_image = Image.open(self.turtle_wins_image_path)
        self.turtle_wins_resized_image = self.turtle_wins_image.resize((294, 95), Image.Resampling.LANCZOS)
        self.turtle_wins_bg_image = ImageTk.PhotoImage(self.turtle_wins_resized_image)

        self.try_again_button_path = "images/try_again.png"
        self.try_again_button_image = Image.open(self.try_again_button_path)
        self.try_again_button_resized_image = self.try_again_button_image.resize((149, 64), Image.Resampling.LANCZOS)
        self.try_again_button_bg_image = ImageTk.PhotoImage(self.try_again_button_resized_image)

        self.arrow_right_image_path = "images/arrow_right.png"
        self.arrow_right_image = Image.open(self.arrow_right_image_path)
        self.arrow_right_resized_image = self.arrow_right_image.resize((88, 81), Image.Resampling.LANCZOS)
        self.arrow_right_bg_image = ImageTk.PhotoImage(self.arrow_right_resized_image)

        self.running = True
        self.root.resizable(False, False)
        self.width = 700
        self.height = 500
        self.root.title("Turtle and Hare Game")
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        self.turtle = Turtle(self.canvas)
        self.hare = Hare(self.canvas)


    def header(self):
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)
        self.canvas.create_image(self.width - 150, 240, anchor=tk.NW, image=self.finish_bg_image)
        self.canvas.create_image(self.width //2 - 20, self.height//2 - 170 , image=self.header_bg_image)
        self.canvas.create_image(self.width // 2 - 120 , self.height // 2 + 120, image=self.arrow_right_bg_image)

    def main_screen(self):  
        self.header()

        start_button = self.canvas.create_image(self.width //2, self.height//2 + 30 , image=self.start_button_bg_image)
        self.canvas.tag_bind(start_button, "<Button-1>", lambda event: self.start_game())

        self.turtle.draw()
        self.hare.draw()

    def start_game(self):
        while self.running :
            self.canvas.delete("all")
            self.header()
            self.turtle.update_position()
            self.hare.update_position()
            self.turtle.draw()
            self.hare.draw()
            if self.turtle.x >= self.width - 170:
               self.win_screen("turtle")
            elif self.hare.x >= self.width - 170:
                self.win_screen("hare")
            self.root.update()
            self.root.after(10)

    def win_screen(self, winner):
        self.running = False
        if winner == "turtle":
            self.canvas.create_image(self.width // 2, self.height // 2 - 40, image=self.turtle_wins_bg_image)
            self.canvas.create_image(self.width // 2, self.height // 2 + 30, image=self.try_again_button_bg_image)
        elif winner == "hare":
            self.canvas.create_image(self.width // 2, self.height // 2 - 40, image=self.hare_wins_bg_image)
            self.canvas.create_image(self.width // 2, self.height // 2 + 30, image=self.try_again_button_bg_image)
        reset_button = self.canvas.create_image(self.width // 2, self.height // 2 + 30,
                                                image=self.try_again_button_bg_image)
        self.canvas.tag_bind(reset_button, "<Button-1>", lambda event: self.reset_game())


    def reset_game(self):
        self.running = True
        self.turtle.x = 50
        self.hare.x = 50
        self.canvas.delete("all")
        self.main_screen()

    def run(self):
        self.main_screen()
        self.root.mainloop()


if __name__ == "__main__":
    game = Game()
    game.run()