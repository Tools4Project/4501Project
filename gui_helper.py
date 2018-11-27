import cv2
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox
from tkinter import filedialog
global_dict = {"pic_fp": "", "filename": "", "art_fp": ""}


def camera_fn(window):
    def camera():
        cap = cv2.VideoCapture(0)
        count = 1
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            if ret is True:
                # Our operations on the frame come here

                # Display the resulting frame
                cv2.imshow('frame', frame)
                k = cv2.waitKey(33)
                if k == ord('q'):
                    break
                elif k == ord('c'):
                    frame = cv2.resize(frame, (256, 144), interpolation=cv2.INTER_CUBIC)
                    cv2.imwrite('./pic' + str(count) + '.jpg', frame)
                    count += 1
        global_dict["filename"] = './pic' + str(count - 1) + '.jpg'
        # When everything is done, release the capture
        global_dict["pic_fp"] = global_dict["filename"]
        cap.release()
        cv2.destroyAllWindows()

        # add the third canvas above the process button and display trained graphs
        img = Image.open(global_dict["pic_fp"])
        img = img.resize((192, 292), Image.ANTIALIAS)
        filename = ImageTk.PhotoImage(img)

        canvas = tk.Canvas(window, height=300, width=200)  # canvas size
        canvas.create_rectangle(0, 0, 200, 300, fill="#476042")
        canvas.place(x=290, y=150)  # canvas position
        canvas.image = filename  # <--- keep reference of your image
        canvas.create_image(102, 6, anchor='n', image=filename)

    return camera


# function to be called when mouse is clicked
# add the first canvas above the upload-art-graph button
def hit_me1_fn(window):
    def hit_me1():
        file = filedialog.askopenfilename(parent=window, initialdir="./", title='Choose an image.')
        if file.lower().endswith('jpg') or file.lower().endswith('jpeg') or file.lower().endswith(
                'png') or file.lower().endswith('bmp'):
            img = Image.open(file)
            img = img.resize((192, 292), Image.ANTIALIAS)  # Reshape the picture into a fixed window
            filename = ImageTk.PhotoImage(img)  # Image.open(file)
        else:
            tkinter.messagebox.showinfo(title='Error', message="Please try to upload a 'jpg','jpeg','png','bmp' file")
            return

        # Save the art_fp
        global_dict["art_fp"] = file
        canvas = tk.Canvas(window, height=300, width=200)  # canvas size
        canvas.create_rectangle(0, 0, 200, 300, fill="#476042")  # set canvas background and proper window to show graph

        canvas.place(x=40, y=150)  # canvas position
        canvas.image = filename  # <--- keep reference of your image
        canvas.create_image(102, 6, anchor='n',
                            image=filename)
        # Anchor points (the middle point at the top of the N picture) is placed in the 250,0 coordinates.

    return hit_me1


# Set upload local pic button

def hit_me2_fn(window):
    def hit_me2():
        window1 = tk.Toplevel(window)
        window1.title('Upload your own picture!')
        window1.geometry('400x300')
        b_via_local = tk.Button(window1, text='Upload via local', font=('Times', 12), width=30, height=3,
                                command=upload_pic_fn(window))
        b_via_camera = tk.Button(window1, text="Upload via camera ", font=('Times', 12), width=30, height=3,
                                 command=camera_fn(window))
        instr_photo = tk.Label(window1, text="'q': to exit; 'c': take a photo", font=('Symbol', 12), width=30, height=1)
        instr_photo.place(x=100, y=140)
        b_via_local.place(x=100, y=80)
        b_via_camera.place(x=100, y=160)

    return hit_me2


# set the second canvas to display local graph above the locat-graph-button
def upload_pic_fn(window):
    def upload_pic():
        file = filedialog.askopenfilename(parent=window, initialdir="./", title='Choose an image.')
        if file.lower().endswith('jpg') or file.lower().endswith('jpeg') or file.lower().endswith(
                'png') or file.lower().endswith('bmp'):
            img = Image.open(file)
            img = img.resize((192, 292), Image.ANTIALIAS)  # Reshape the picture into a fixed window
            filename = ImageTk.PhotoImage(img)  # Image.open(file)
        else:
            tkinter.messagebox.showinfo(title='Error', message="Please try to upload a 'jpg','jpeg','png','bmp' file")
            return
            # Save pic_fp
        global_dict["pic_fp"] = file
        canvas = tk.Canvas(window, height=300, width=200)  # canvas size
        canvas.create_rectangle(0, 0, 200, 300, fill="#476042")
        canvas.place(x=290, y=150)  # canvas position
        canvas.image = filename  # <--- keep reference of your image
        canvas.create_image(102, 6, anchor='n',
                            image=filename)
        # Anchor points (the middle point at the top of the N picture) is placed in the 250,0 coordinates.

    return upload_pic
