from tkinter import *
import random

WIDTH = 500
HEIGHT = 700


class Ball:
    def __init__(self, canvas, paddle, color,):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.x = 0
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.canvas.bind_all('<KeyPress-Return>', self.start)

    def start(self,event):
        self.x = random.choice((-3, -2, -1, 1, 2, 3))
        self.y =-3

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True

        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = abs(self.y)

        if pos[3] >= self.canvas_height:
            # self.y = abs(self.y) * -1
            self.hit_bottom = True

        if pos[0] <= 0:
            self.x = abs(self.x)

        if pos[2] >= self.canvas_width:
            self.x = abs(self.x) * -1

        if self.hit_paddle(pos):
            paddle_pos = self.canvas.coords(self.paddle.id)
            if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                    return True

            return False

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, event):
        self.x = -2

    def turn_right(self, event):
        self.x = 2


class Block:
    def __init__(self,x,y,canvas,color):
        self.canvas =canvas
        self.pos_x = x
        self.pos_y = y
        self.id =canvas.create_rectangle(0,0,50,20, fill=color)
        self.canvas.move(self.id, 25 + self.pos_x * 50, 25 + self.pos_y * 20)

    def delete(self):
        self.canvas.delete(self.id)

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
c = Canvas(tk, width=WIDTH, height=HEIGHT, bd=0, highlightthickness=0)
c.pack()
tk.update()

p = Paddle(c, 'navy')

ball = Ball(c, p, 'yellow')

def update():

    if not ball.hit_bottom:
        ball.draw()
        p.draw()

    tk.update_idletasks()
    tk.after(10,update)

tk.after(10,update)
tk.mainloop()
