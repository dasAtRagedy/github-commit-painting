import tkinter as tk

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

def styled_button(root, text, command):
    # Initialize the button with text, custom font, and command
    button = tk.Button(root, text=text, command=command,
                       bg='#4CAF50', fg='white', activebackground='#45a049')
    
    # Add hover effect
    def on_hover(event):
        button['bg'] = '#45a049'
        
    def on_leave(event):
        button['bg'] = '#4CAF50'
        
    button.bind("<Enter>", on_hover)
    button.bind("<Leave>", on_leave)
    
    return button

