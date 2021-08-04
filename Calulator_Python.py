from tkinter import *
import tkinter.font as font


window = Tk()
window.title("Simple Calculator")
# Set window size
window.geometry("463x500")
# Set window background color
window.configure(bg="#999999")
# Label for displaying contents
display_label = Label(window, bg='#999999', text="")
display_label.place(relx='0.01', rely='0.06', height='95', width='440')
# Adding Calculator buttons
myFont = font.Font(family='Helvetica', size=20, weight='bold')

# Num Buttons
seven_button = Button(window, text='7', bg='light grey')
seven_button.place(x=7, y=135, height=90, width=90)
seven_button['font'] = myFont

eight_button = Button(window, text='8', bg='light grey')
eight_button.place(x=97, y=135, height=90, width=90)
eight_button['font'] = myFont

nine_button = Button(window, text='9', bg='light grey')
nine_button.place(x=187, y=135, height=90, width=90)
nine_button['font'] = myFont

four_button = Button(window, text='4', bg='light grey')
four_button.place(x=7, y=225, height=90, width=90)
four_button['font'] = myFont

five_button = Button(window, text='5', bg='light grey')
five_button.place(x=97, y=225, height=90, width=90)
five_button['font'] = myFont

six_button = Button(window, text='6', bg='light grey')
six_button.place(x=187, y=225, height=90, width=90)
six_button['font'] = myFont

one_button = Button(window, text='1', bg='light grey')
one_button.place(x=7, y=315, height=90, width=90)
one_button['font'] = myFont

two_button = Button(window, text='2', bg='light grey')
two_button.place(x=97, y=315, height=90, width=90)
two_button['font'] = myFont

three_button = Button(window, text='3', bg='light grey')
three_button.place(x=187, y=315, height=90, width=90)
three_button['font'] = myFont

dbl_zero_button = Button(window, text='00', bg='light grey')
dbl_zero_button.place(x=7, y=405, height=90, width=90)
dbl_zero_button['font'] = myFont

zero_button = Button(window, text='0', bg='light grey')
zero_button.place(x=97, y=405, height=90, width=90)
zero_button['font'] = myFont

point_button = Button(window, text=".", bg='light grey')
point_button.place(x=187, y=405, height=90, width=90)
point_button['font'] = myFont


# Operation Buttons

plus_button = Button(window, text='+', bg='light grey')
plus_button.place(x=277, y=405, height=90, width=90)
plus_button['font'] = myFont

minus_button = Button(window, text='-', bg='light grey')
minus_button.place(x=277, y=315, height=90, width=90)
minus_button['font'] = myFont

into_button = Button(window, text='x', bg='light grey')
into_button.place(x=277, y=225, height=90, width=90)
into_button['font'] = myFont

div_button = Button(window, text='/', bg='light grey')
div_button.place(x=277, y=135, height=90, width=90)
div_button['font'] = myFont

clear_button = Button(window, text='AC', bg='light grey')
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