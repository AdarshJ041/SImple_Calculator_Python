from tkinter import *

window = Tk()
window.title("Simple Calculator")
# Set window size
window.geometry("450x550")
# Set window background color
window.configure(bg="#999999")
# Label for displaying contents
display_label = Label(window, bg='white', text="")
display_label.place(relx='0.01', rely='0.06', height='95', width='440')

# Num Buttons
seven_button = Button(window, text='7')
seven_button.place(x=10, y=140, height=90, width=90)

eight_button = Button(window, text='8')
eight_button.place(x=120, y=140, height=90, width=90)

nine_button = Button(window, text='9')
nine_button.place(x=230, y=140, height=90, width=90)

four_button = Button(window, text='4')
four_button.place(x=10, y=240, height=90, width=90)

five_button = Button(window, text='5')
five_button.place(x=120, y=240, height=90, width=90)

six_button = Button(window, text='6')
six_button.place(x=230, y=240, height=90, width=90)

one_button = Button(window, text='1')
one_button.place(x=10, y=340, height=90, width=90)

two_button = Button(window, text='2')
two_button.place(x=120, y=340, height=90, width=90)

three_button = Button(window, text='3')
three_button.place(x=230, y=340, height=90, width=90)

dbl_zero_button = Button(window, text='00')
dbl_zero_button.place(x=10, y=440, height=90, width=90)

zero_button = Button(window, text='0')
zero_button.place(x=120, y=440, height=90, width=90)

point_button = Button(window, text=".")
point_button.place(x=230, y=440, height=90, width=90)

window.mainloop()