import tkinter as tk
from gui_helper import global_dict, hit_me1_fn, hit_me2_fn
from cnn_model import cnn_paint_style_fn
from PIL import Image, ImageTk

def main():
    window = tk.Tk()
    window.title('Welcome to our project!')

    # Set the size of the window
    window.geometry('800x600')

    canvas = tk.Canvas(window, height=600, width=1000)
    canvas.pack()
    image = Image.open('./background.jpg')
    image = image.resize((800, 600), Image.ANTIALIAS)
    photo_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=photo_image, anchor="nw")

    canvas_header = canvas.create_text(130, 40, anchor="nw")
    title_ = 'Welcome to our project (Paint Style Transformation)'
    canvas.itemconfig(canvas_header, text=title_, width=800)
    canvas.itemconfig(canvas_header, font=('Times', 25, 'bold'))
    canvas.insert(canvas_header, 0, '')

    canvas_author = canvas.create_text(420, 95, anchor="nw")
    text_ = 'Author: Tao Li, Jianxing Wan, Xiaojian Fan, Jiali Sun'
    canvas.itemconfig(canvas_author, text=text_, width=800)
    canvas.itemconfig(canvas_author, font=('Times', 16, 'italic'))
    canvas.insert(canvas_author, 0, '')

    # Set the canvas to show the process of deep learning

    b_upload_art = tk.Button(window, text='Upload Art', font=('Times', 11), width=15, height=5,
                             command=hit_me1_fn(window))
    b_upload_art.place(x=70, y=500)

    b_upload_pic = tk.Button(window, text='Upload Yor Picture', font=('Times', 11), width=15, height=5,
                             command=hit_me2_fn(window))
    b_upload_pic.place(x=340, y=500)

    b_upload_pic = tk.Button(window, text='Process', font=('Times', 11), width=15, height=5,
                             command=cnn_paint_style_fn(window, global_dict))
    b_upload_pic.place(x=600, y=500)

    window.mainloop()


if __name__ == '__main__':
    main()
