import tkinter as tk

from .custom_components import round_rectangle, styled_button
from .utils import ColorPalette, get_initial_offset, is_leap_year
from .git_logic import main as git_main

class CommitBox:
    def __init__(self, canvas:tk.Canvas, x1:int, y1:int, x2:int, y2:int):
        self.canvas = canvas
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.color_palette = [color.value for color in ColorPalette]
        self.current_index = 0
        self.rectangle = round_rectangle(canvas, x1, y1, x2, y2, radius=(int(abs(y2-y1)/2)), fill=self.color_palette[0])
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
    

def start_app(*, year:int):
    global root
    root = tk.Tk()
    root.title("gitPaint.exe")
    root['bg'] = '#0d1117'
    root.resizable(width=False, height=False)
    # root.geometry("800x300")

    global canvas
    box_size = 10
    box_margin = 2
    canvas_height = 7*box_size + (7+1)*box_margin
    canvas_width = 53*box_size + (53+1)*box_margin

    canvas = tk.Canvas(root, bg="#0d1117", height=canvas_height, width=canvas_width, highlightthickness=0)
    canvas.pack(anchor='w')

    box_columns = draw_canvas(box_size=box_size, box_margin=box_margin, year=year)
    boxes = [box for column in box_columns for box in column]

    frame_committer_email = tk.Frame(root)
    label_committer_email = tk.Label(frame_committer_email, text="Committer Email:", bg="#0d1117", fg="white").pack(side=tk.LEFT)
    entry_committer_email = tk.Entry(frame_committer_email)
    entry_committer_email.pack()
    frame_committer_email.pack(anchor='w')

    frame_committer_name = tk.Frame(root)
    label_committer_name = tk.Label(frame_committer_name, text="Committer Name:", bg="#0d1117", fg="white").pack(side=tk.LEFT)
    entry_committer_name = tk.Entry(frame_committer_name)
    entry_committer_name.pack()
    frame_committer_name.pack(anchor='w')

    button_generate = styled_button(root, "Create!", lambda: git_main(commits=[box.current_index for box in boxes], year=year, committer_email=entry_committer_email.get(), committer_name=entry_committer_name.get()))
    button_generate.pack(anchor='w')

    root.mainloop()

def draw_canvas(*, box_size:int = 10, box_margin:int = 2, year:int) -> list[str]:
    boxes = []
    current_box = 0
    initial_box_offset = (get_initial_offset(year)+1)%7
    days_in_year = 366 if is_leap_year(year) else 365

    for week in range(54):
        cols = []
        for day in range(7):
            if current_box - initial_box_offset >= days_in_year:
                break
            if current_box >= initial_box_offset:
                box = CommitBox(canvas, 
                                box_margin*(1+week)+week*box_size, box_margin*(1+day)+day*box_size, 
                                box_margin*(1+week)+week*box_size+box_size, box_margin*(1+day)+day*box_size+box_size)
                cols.append(box)
            current_box += 1
        boxes.append(cols)

    return boxes
