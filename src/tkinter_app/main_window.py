import tkinter as tk

class CommitBox:
    def __init__(self, canvas:tk.Canvas, x1:int, y1:int, x2:int, y2:int, color_palette:list[str] = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]):
        self.canvas = canvas
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.color_palette = color_palette
        self.current_index = 0
        self.rectangle = canvas.create_round_rectangle(x1, y1, x2, y2, radius=(int(abs(y2-y1)/2)), fill=self.color_palette[0])
        canvas.tag_bind(self.rectangle, "<Button-1>", self.left_click)
        # Different right click buttons for different systems
        canvas.tag_bind(self.rectangle, "<Button-2>", self.right_click)
        canvas.tag_bind(self.rectangle, "<Button-3>", self.right_click)
    
    def left_click(self, event):
        if self.current_index < len(self.color_palette)-1: self.current_index += 1
        self.update_color()

    def right_click(self, event):
        if self.current_index > 0: self.current_index -= 1
        self.update_color()
    
    def update_color(self):
        self.canvas.itemconfig(self.rectangle, fill=self.color_palette[self.current_index])
    

def start_app():
    global root
    root = tk.Tk()
    root.title("gitPaint.exe")
    root['bg'] = '#0d1117'
    # root.geometry("800x300")

    global canvas
    box_size = 10
    box_margin = 2
    canvas_height = 7*box_size + (7+1)*box_margin
    canvas_width = 53*box_size + (53+1)*box_margin

    canvas = tk.Canvas(root, bg="#0d1117", height=canvas_height, width=canvas_width, highlightthickness=0)
    canvas.pack()

    # dirty monkey patching
    canvas.create_round_rectangle = lambda x1, y1, x2, y2, radius, **kwargs: round_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs)

    draw_canvas(box_size, box_margin)

    root.mainloop()

def draw_canvas(box_size:int = 10, box_margin:int = 2) -> list[str]:
    boxes = []
    current_box = 0
    current_year = 2023
    initial_box_offset = (get_initial_offset(current_year)+1)%7
    days_in_year = 366 if is_leap_year(current_year) else 365

    for i in range(53):
        row = []
        for j in range(7):
            if current_box + initial_box_offset >= days_in_year:
                break
            if current_box >= initial_box_offset:
                box = CommitBox(canvas, box_margin*(1+i)+i*box_size, box_margin*(1+j)+j*box_size, box_margin*(1+i)+i*box_size+box_size, box_margin*(1+j)+j*box_size+box_size)
                row.append(box)
            current_box += 1
        boxes.append(row)

    return boxes

def round_rectangle(canvas:tk.Canvas, x1:int, y1:int, x2:int, y2:int, radius:int=25, **kwargs) -> int:
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

def get_initial_offset(year:int) -> int:
    from datetime import datetime
    return datetime(year, 1, 1).weekday()

def is_leap_year(year:int) -> bool:
    return year%4 == 0 and (year % 400 == 0 or year % 100 != 0)
