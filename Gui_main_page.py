#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 17:13:02 2018

@author: jl_s
"""

import tkinter as tk
window = tk.Tk()
window.title('Welcome to our project!')

# Set the size of the window
window.geometry('800x600')

# set the header
title_ = 'Welcome to our project (Paint Styple Transformation)'
header = tk.Label(window,text = title_,bg = 'green',font = ('Arial', 22),width=50, height=2)
header.place(x=65,y=10)

# set the Author
text_ = 'Author: Tao Li, Jianxing, Xiaojian Fan, Jiali Sun'
group_mem = tk.Label(window, text=text_, bg='white', font=('Arial', 16), width=35, height=1)
group_mem.place(x=450,y=70)

# Set upload art button
def hit_me1():
    pass

b_upload_art = tk.Button(window, text='Upload Art', font=('Arial', 12), width=30, height=3, command=hit_me1)
b_upload_art.place(x=50,y=450)

# Set upload pic button
def hit_me2():
    pass

b_upload_pic = tk.Button(window, text='Upload Art', font=('Arial', 12), width=30, height=3, command=hit_me2)
b_upload_pic.place(x=300,y=450)

# Set process button
def hit_me3():
    pass

b_upload_pic = tk.Button(window, text='Process', font=('Arial', 12), width=30, height=3, command=hit_me3)
b_upload_pic.place(x=550,y=450)

window.mainloop()
