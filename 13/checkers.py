import tkinter as tk

win = tk.Tk()
canvas = tk.Canvas(win, bg='brown', width=400, height=400)
for i in range(8):
    canvas.create_line((0, 50 * i), (400, 50 * i))
    canvas.create_line((50 * i, 0), (50 * i, 400))
for i in range(8):
    for j in range(3):
        if (i + j) % 2 == 0:
            canvas.create_oval((50 * i, 50 * j), (50 * (i + 1), 50 * (j + 1)), fill="black")
        if (i + (j+5)) % 2 == 0:
            canvas.create_oval((50 * i, 50 * (j+5)), (50 * (i + 1), 50 * ((j+5) + 1)), fill="white")
canvas.pack()
win.mainloop()
