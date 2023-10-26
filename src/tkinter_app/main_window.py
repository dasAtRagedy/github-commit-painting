import tkinter as tk

class CommitBox:
    def __init__(self, canvas, x1, y1, x2, y2, initial_color="white"):
        self.canvas = canvas
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.color = initial_color
        self.rectangle = canvas.create_rectangle(x1, y1, x2, y2, fill=initial_color)
        canvas.tag_bind(self.rectangle, "<Button-1>", self.left_click)
        # Different right click buttons for different systems
        canvas.tag_bind(self.rectangle, "<Button-2>", self.right_click)
        canvas.tag_bind(self.rectangle, "<Button-3>", self.right_click)
    
    def left_click(self, event):
        self.color = "red"
        self.update_color()

    def right_click(self, event):
        self.color = "green"
        self.update_color()
    
    def update_color(self):
        self.canvas.itemconfig(self.rectangle, fill=self.color)
    

def on_click(event):
    item = canvas.find_closest(event.x, event.y)
    current_color = canvas.itemcget(item, "fill")
    new_color = "red" if current_color != "red" else "green"
    canvas.itemconfig(item, fill=new_color)

def start_app():
    global root
    root = tk.Tk()
    root.title("My Tkinter App")
    # root.geometry("800x300")

    global canvas
    box_size = 10
    box_margin = int(box_size*0.2)
    canvas_height = 7*box_size + (7+1)*box_margin
    canvas_width = 53*box_size + (53+1)*box_margin
    canvas = tk.Canvas(root, bg="white", height=canvas_height, width=canvas_width)
    canvas.pack()

    draw_canvas(box_size, box_margin)

    root.mainloop()

def draw_canvas(box_size = 10, box_margin = 2):
    boxes = []

    for i in range(53):
        row = []
        for j in range(7):
            box = CommitBox(canvas, box_margin*(1+i)+i*box_size, box_margin*(1+j)+j*box_size, box_margin*(1+i)+i*box_size+box_size, box_margin*(1+j)+j*box_size+box_size)
            row.append(box)
        boxes.append(row)
