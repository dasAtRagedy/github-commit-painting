import tkinter as tk

class CommitBox:
    def __init__(self, canvas, x1, y1, x2, y2, initial_color="white"):
        self.canvas = canvas
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.color = initial_color
        self.rectangle = canvas.create_round_rectangle(x1, y1, x2, y2, radius=(int(abs(y2-y1)/2)), fill=initial_color, outline="black")
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
    

def start_app():
    global root
    root = tk.Tk()
    root.title("My Tkinter App")
    # root.geometry("800x300")

    global canvas
    box_size = 10
    box_margin = 2
    canvas_height = 7*box_size + (7+1)*box_margin
    canvas_width = 53*box_size + (53+1)*box_margin

    canvas = tk.Canvas(root, bg="white", height=canvas_height, width=canvas_width)
    canvas.pack()

    # dirty monkey patching
    canvas.create_round_rectangle = lambda x1, y1, x2, y2, radius, **kwargs: round_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs)

    draw_canvas(box_size, box_margin)

    root.mainloop()

def draw_canvas(box_size = 10, box_margin = 2):
    boxes = []
    current_day = 0

    for i in range(53):
        row = []
        for j in range(7):
            box = CommitBox(canvas, box_margin*(1+i)+i*box_size, box_margin*(1+j)+j*box_size, box_margin*(1+i)+i*box_size+box_size, box_margin*(1+j)+j*box_size+box_size)
            row.append(box)
            current_day += 1
        boxes.append(row)

def round_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)
