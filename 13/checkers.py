import tkinter as tk

current_item = None
plain = [[0] * 8 for _ in range(8)]


def get_type(tag):
    if tag in 'checker2':
        return -1
    return 1


def mouse_pos(event):
    global x
    global y
    global plain
    global current_item
    x = event.x
    y = event.y
    if current_item is not None:
        if plain[x // 50][y // 50] == 0 and abs(x//50 - current_item[0]) == 1 and abs(y//50 - current_item[1]) == 1:
            item = canvas.find_closest(current_item[0] * 50 + 25, current_item[1] * 50 + 25)
            plain[current_item[0]][current_item[1]] = 0
            plain[x // 50][y // 50] = get_type(canvas.itemcget(item, 'tags'))
            canvas.moveto(item, (x // 50) * 50, (y // 50) * 50)
            current_item = (x // 50, y // 50)

def click_oval(event):
    global current_item
    if current_item is None:
        current_item = (x // 50, y // 50)
    elif plain[x//50][y//50] != plain[current_item[0]][current_item[1]]:
            new_i = 2*(x//50) - current_item[0]
            new_j = 2*(y//50) - current_item[1]
            if -1 < new_j < 8 and -1 < new_i < 8 and plain[new_i][new_j] == 0:
                item = canvas.find_closest(current_item[0] * 50 + 25, current_item[1] * 50 + 25)
                plain[current_item[0]][current_item[1]] = 0
                plain[x//50][y//50] = 0
                canvas.delete(canvas.find_closest(x,y))
                plain[new_i][new_j] = get_type(canvas.itemcget(item, 'tags'))
                canvas.moveto(item, (new_i) * 50, (new_j) * 50)
                current_item = None
    else:
        current_item = None


win = tk.Tk()
canvas = tk.Canvas(win, bg='brown', width=400, height=400)
for i in range(8):
    canvas.create_line((0, 50 * i), (400, 50 * i))
    canvas.create_line((50 * i, 0), (50 * i, 400))
for i in range(8):
    for j in range(3):
        if (i + j) % 2 == 0:
            canvas.create_oval((50 * i, 50 * j), (50 * (i + 1), 50 * (j + 1)), fill="black", activewidth=2,
                               activeoutline="#0ff", tags="checker1")
            plain[i][j] = 1
        if (i + (j + 5)) % 2 == 0:
            canvas.create_oval((50 * i, 50 * (j + 5)), (50 * (i + 1), 50 * ((j + 5) + 1)), fill="white", activewidth=2,
                               activeoutline="#0ff", tags="checker2")
            plain[i][j + 5] = -1

x, y = 0, 0
win.bind('<Motion>', mouse_pos)
canvas.tag_bind("checker1", "<ButtonPress-1>", click_oval)
canvas.tag_bind("checker2", "<ButtonPress-1>", click_oval)
canvas.pack()
win.mainloop()
