from functools import partial
from tkinter import Tk, BOTH, Frame, Button
import tkinter.messagebox as message
from tkinter.ttk import Style, Label
import tkinter as tk


class Caro(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.Buttons = {}
        self.memory = []
        self.Ox = 10
        self.Oy = 10
        self.initUI()

    def initUI(self):
        self.parent.title("Caro")
        self.pack(fill=BOTH, expand=1)
        self.style = Style()
        self.style.theme_use("clam")
        self.createMainBoard()

    def renderButton(self, x=1, y=1, height=1, width=1, command=None, bg="white", bwidth="2"):
        button = tk.Button(self, command=command, height=height,
                           width=width, bg=bg, borderwidth=bwidth)
        button.place(x=x, y=y)
        return button

    def renderLabel(self, title, x, y):
        label = Label(self, text=title)
        label.place(x=x, y=y)

    def createMainBoard(self):
        for x in range(self.Ox):
            for y in range(self.Oy):
                self.Buttons[x, y] = self.renderButton(
                    height=1, width=1, command=partial(self.handleChoose, x, y), bg="gray")
                self.Buttons[x, y].grid(row=x, column=y)

    def handleChoose(self, x=0, y=0):
        if self.Buttons[x, y]["text"] == "":
            if len(self.memory) == 0:
                self.memory.append(0)
                self.Buttons[x, y]["text"] = "O"
                self.Buttons[x, y].config(bg="red")
                if self.checkWin(x, y, "O"):
                    self.notification("Winner", "O win")
                    self.newGame()
            elif self.memory[-1] == 0:
                self.memory.append(1)
                self.Buttons[x, y]["text"] = "X"
                self.Buttons[x, y].config(bg="blue")
                if self.checkWin(x, y, "X"):
                    self.notification("Winner", "X win")
                    self.newGame()

            else:
                self.memory.append(0)
                self.Buttons[x, y]["text"] = "O"
                self.Buttons[x, y].config(bg="red")
                if self.checkWin(x, y, "O"):
                    self.notification("Winner", "O win")
                    self.newGame()

    def notification(self, title, msg):
        message.showinfo(str(title), str(msg))

    def checkWin(self, x, y, XO):
        # row
        count = 0
        i, j = x, y
        while(j < self.Oy and self.Buttons[i, j]["text"] == XO):
            j += 1
            count += 1
        i, j = x, y
        while (j > 0 and self.Buttons[i, j]["text"] == XO):
            j -= 1
            count += 1
        if count == 6:
            return True
        # col
        count = 0
        i, j = x, y
        print(i, j)
        while (i < self.Ox and self.Buttons[i, j]["text"] == XO):
            i += 1
            count += 1
        i, j = x, y
        while (i >= 0 and self.Buttons[i, j]["text"] == XO):
            i -= 1
            count += 1
        if count == 6:
            return True
        # right
        count = 0
        i, j = x, y
        while (i >= 0 and j < self.Oy and self.Buttons[i, j]["text"] == XO):
            count += 1
            i -= 1
            j += 1
        i, j = x, y
        while(i < self.Ox and j < self.Oy and self.Buttons[i, j]["text"] == XO):
            count += 1
            i += 1
            j += 1
        if count == 6:
            return True
        # left
        count = 0
        i, j = x, y
        while(j >= 0 and i < self.Ox and self.Buttons[i, j]["text"] == XO):
            j -= 1
            i += 1
            count += 1
        i, j = x, y
        while (i >= 0 and j >= 0 and self.Buttons[i, j]["text"] == XO):
            j -= 1
            i -= 1
            count += 1
        if count == 6:
            return True
        return False

    def newGame(self):
        self.memory.clear()
        for i in range(self.Ox):
            for j in range(self.Oy):
                self.Buttons[i, j]["text"] = ""
                self.Buttons[i, j].config(bg="gray")


root = Tk()
# root.geometry("400x400")
app = Caro(root)
root.mainloop()
