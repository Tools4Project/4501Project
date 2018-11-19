import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

window = tk.Tk()
window.title('Welcome to our project!')

# Set the size of the window
window.geometry('800x600')

# set the header
title_ = 'Welcome to our project (Paint Style Transformation)'
header = tk.Label(window, text=title_, bg='green', font=('Arial', 22), width=50, height=2)
header.place(x=65, y=10)

# set the Author
text_ = 'Author: Tao Li, Jianxing, Xiaojian Fan, Jiali Sun'
group_mem = tk.Label(window, text=text_, bg='white', font=('Arial', 16), width=35, height=1)
group_mem.place(x=450, y=70)

# Set the canvas to show the process of deep learning
canvas = tk.Canvas(window, bg='white', height=200, width=500)
canvas.place(x=50, y=150)


# function to be called when mouse is clicked
def hit_me1():
    File = filedialog.askopenfilename(parent=window, initialdir="/", title='Choose an image.')
    filename = ImageTk.PhotoImage(Image.open(File))
    canvas.image = filename  # <--- keep reference of your image
    canvas.create_image(50, 1, anchor='n', image=filename)


b_upload_art = tk.Button(window, text='Upload Art', font=('Arial', 12), width=30, height=3, command=hit_me1)
b_upload_art.place(x=50, y=450)


# Set upload pic button



def hit_me2():
    window1 = tk.Toplevel(window)
    window1.title('Upload your own picture!')
    window1.geometry('400x300')
    b_via_local = tk.Button(window1, text='Upload via local', font=('Arial', 12), width=30, height=3, command=upload_pic)
    b_via_camera = tk.Button(window1, text='Upload via camera', font=('Arial', 12), width=30, height=3, command=upload_camera)
    b_via_local.place(x=100, y=80)
    b_via_camera.place(x=100, y=160)

def upload_pic():
    File = filedialog.askopenfilename(parent=window, initialdir="/", title='Choose an image.')
    filename = ImageTk.PhotoImage(Image.open(File))
    canvas.image = filename  # <--- keep reference of your image
    canvas.create_image(50, 1, anchor='n', image=filename)
    pass

def upload_camera():
    pass

b_upload_pic = tk.Button(window, text='Upload Yor Picture', font=('Arial', 12), width=30, height=3, command=hit_me2)
b_upload_pic.place(x=300, y=450)


# Set process button
def hit_me3():
    pass


b_upload_pic = tk.Button(window, text='Process', font=('Arial', 12), width=30, height=3, command=hit_me3)
b_upload_pic.place(x=550, y=450)

window.mainloop()
