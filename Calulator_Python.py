from tkinter import *
import tkinter.font as font
from tkinter import Button

window = Tk()
window.title("Simple Calculator")
# Set window size
window.geometry("463x500")
# Set window background color
window.configure(bg="#999999")
# Label for displaying contents
display_label = Label(window, bg='#999999', text="", font=("Arial", 25), anchor='e')
display_label.place(relx='0.01', rely='0.06', height='95', width='450')
# Adding Calculator buttons
myFont = font.Font(family='Helvetica', size=20, weight='bold')

any_operator_clicked = False
plus_op_clicked = False
minus_op_clicked = False
into_op_clicked = False
div_op_clicked = False
per_op_clicked = False
old_value = 0.0


# Num Buttons
def seven_button_clicked():
    svn_btn = True
    if svn_btn:
        display_label.config(text=display_label.cget('text') + '7')


seven_button = Button(window, text='7', bg='light grey', command=seven_button_clicked)
seven_button.place(x=7, y=135, height=90, width=90)
seven_button['font'] = myFont


def eight_button_clicked():
    egt_btn = True
    if egt_btn:
        display_label.config(text=display_label.cget('text') + '8')


eight_button = Button(window, text='8', bg='light grey', command=eight_button_clicked)
eight_button.place(x=97, y=135, height=90, width=90)
eight_button['font'] = myFont


def nine_button_clicked():
    nine_btn = True
    if nine_btn:
        display_label.config(text=display_label.cget('text') + '9')


nine_button = Button(window, text='9', bg='light grey', command=nine_button_clicked)
nine_button.place(x=187, y=135, height=90, width=90)
nine_button['font'] = myFont


def four_button_clicked():
    fr_btn = True
    if fr_btn:
        display_label.config(text=display_label.cget('text') + '4')


four_button = Button(window, text='4', bg='light grey', command=four_button_clicked)
four_button.place(x=7, y=225, height=90, width=90)
four_button['font'] = myFont


def five_button_clicked():
    fiv_btn = True
    if fiv_btn:
        display_label.config(text=display_label.cget('text') + '5')


five_button = Button(window, text='5', bg='light grey', command=five_button_clicked)
five_button.place(x=97, y=225, height=90, width=90)
five_button['font'] = myFont


def six_button_clicked():
    sx_btn = True
    if sx_btn:
        display_label.config(text=display_label.cget('text') + '6')


six_button = Button(window, text='6', bg='light grey', command=six_button_clicked)
six_button.place(x=187, y=225, height=90, width=90)
six_button['font'] = myFont


def one_button_clicked():
    one_btn = True
    if one_btn:
        display_label.config(text=display_label.cget('text') + '1')


one_button = Button(window, text='1', bg='light grey', command=one_button_clicked)
one_button.place(x=7, y=315, height=90, width=90)
one_button['font'] = myFont


def two_button_clicked():
    two_btn = True
    if two_btn:
        display_label.config(text=display_label.cget('text') + '2')


two_button = Button(window, text='2', bg='light grey', command=two_button_clicked)
two_button.place(x=97, y=315, height=90, width=90)
two_button['font'] = myFont


def three_button_clicked():
    thr_btn = True
    if thr_btn:
        display_label.config(text=display_label.cget('text') + '3')


three_button = Button(window, text='3', bg='light grey', command=three_button_clicked)
three_button.place(x=187, y=315, height=90, width=90)
three_button['font'] = myFont


def dbl_zero_button_clicked():
    dbl_zro_btn = True
    if dbl_zro_btn:
        display_label.config(text=display_label.cget('text') + '00')


dbl_zero_button: Button = Button(window, text='00', bg='light grey', command=dbl_zero_button_clicked)
dbl_zero_button.place(x=7, y=405, height=90, width=90)
dbl_zero_button['font'] = myFont


def zero_button_clicked():
    zro_btn = True
    if zro_btn:
        display_label.config(text=display_label.cget('text') + '0')


zero_button = Button(window, text='0', bg='light grey', command=zero_button_clicked)
zero_button.place(x=97, y=405, height=90, width=90)
zero_button['font'] = myFont


def point_button_clicked():
    pt_btn = True
    if pt_btn:
        display_label.config(text=display_label.cget('text') + '.')


point_button = Button(window, text=".", bg='light grey', command=point_button_clicked)
point_button.place(x=187, y=405, height=90, width=90)
point_button['font'] = myFont


def operator_clicked():
    global any_operator_clicked
    any_operator_clicked = True
    global old_value
    old_value = display_label.cget('text')
    display_label.config(text='')
    try:
        old_value = float(old_value)
        return old_value
    except ValueError:
        old_value = 0.0
    if old_value == "":
        old_value = 0.0
    else:
        old_value = float(old_value)


# Operation Buttons
def plus_button_clicked():
    global plus_op_clicked
    plus_op_clicked = True
    operator_clicked()


plus_button = Button(window, text='+', bg='light grey', command=plus_button_clicked)
plus_button.place(x=277, y=405, height=90, width=90)
plus_button['font'] = myFont


def minus_button_clicked():
    global plus_op_clicked
    plus_op_clicked = False
    global minus_op_clicked
    minus_op_clicked = True
    operator_clicked()


minus_button = Button(window, text='-', bg='light grey', command=minus_button_clicked)
minus_button.place(x=277, y=315, height=90, width=90)
minus_button['font'] = myFont


def into_button_clicked():
    global plus_op_clicked
    plus_op_clicked = False
    global minus_op_clicked
    minus_op_clicked = False
    global into_op_clicked
    into_op_clicked = True
    operator_clicked()


into_button = Button(window, text='x', bg='light grey', command=into_button_clicked)
into_button.place(x=277, y=225, height=90, width=90)
into_button['font'] = myFont


def div_button_clicked():
    global plus_op_clicked
    plus_op_clicked = False
    global minus_op_clicked
    minus_op_clicked = False
    global into_op_clicked
    into_op_clicked = False
    global div_op_clicked
    div_op_clicked = True
    operator_clicked()


div_button = Button(window, text='/', bg='light grey', command=div_button_clicked)
div_button.place(x=277, y=135, height=90, width=90)
div_button['font'] = myFont


def clear_button_clicked():
    display_label.config(text="")


clear_button = Button(window, text='AC', bg='light grey', command=clear_button_clicked)
clear_button.place(x=367, y=135, height=90, width=90)
clear_button['font'] = myFont

backspace_button = Button(window, text='CE', bg='light grey')
backspace_button.place(x=367, y=225, height=90, width=90)
backspace_button['font'] = myFont

percent_button = Button(window, text='%', bg='light grey')
percent_button.place(x=367, y=315, height=90, width=90)
percent_button['font'] = myFont

equal_button = Button(window, text='=', bg='light grey')
equal_button.place(x=367, y=405, height=90, width=90)
equal_button['font'] = myFont

window.mainloop()
