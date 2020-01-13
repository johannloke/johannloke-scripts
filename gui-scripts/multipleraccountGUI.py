from tkinter import *

root = Tk()
root.title("DBS Multipler Account App")

e = Entry(root, width = 35, borderwidth = 30)
e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 20)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

def one_interest():
    global interest
    if f_num < 2000:
        interest = 0.005
    elif 2000 <= f_num < 2500:
        interest = 0.0155
    elif 2500 <= f_num < 5000:
        interest = 0.0185
    elif 5000 <= f_num < 15000:
        interest = 0.019
    elif 15000 <= f_num < 30000:
        interest = 0.02
    else:
        interest = 0.0208

def two_interest():
    global interest
    if f_num < 2000:
        interest = 0.005
    elif 2000 <= f_num < 2500:
        interest = 0.0180
    elif 2500 <= f_num < 5000:
        interest = 0.02
    elif 5000 <= f_num < 15000:
        interest = 0.022
    elif 15000 <= f_num < 30000:
        interest = 0.023
    else:
        interest = 0.035

def three_ormore_interest():
    global interest
    if f_num < 2000:
        interest = 0.005
    elif 2000 <= f_num < 2500:
        interest = 0.02
    elif 2500 <= f_num < 5000:
        interest = 0.022
    elif 5000 <= f_num < 15000:
        interest = 0.024
    elif 15000 <= f_num < 30000:
        interest = 0.025
    else:
        interest = 0.038  


def button_equal():

    e.insert(0, f_num * float(interest))



#Define Buttons
button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda : button_click(1))
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda : button_click(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda : button_click(3))
button_4 = Button(root, text = "4", padx = 40, pady = 20, command =  lambda : button_click(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command =  lambda : button_click(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command =  lambda : button_click(6))
button_7 = Button(root, text = "7", padx = 40, pady = 20, command =  lambda : button_click(7))
button_8 = Button(root, text = "8", padx = 40, pady = 20, command =  lambda : button_click(8))
button_9 = Button(root, text = "9", padx = 40, pady = 20, command =  lambda : button_click(9))
button_0 = Button(root, text = "0", padx = 40, pady = 20, command =  lambda : button_click(0))
button_one_category = Button(root, text = "1 Category", padx = 14, pady = 20, command = one_interest)
button_two_category = Button(root, text = "2 Category", padx = 14, pady = 20, command = two_interest)
button_three_category = Button(root, text = "3 Category", padx = 14, pady = 20, command = three_ormore_interest)
button_four_category = Button(root, text = "4 Category", padx = 14, pady = 20, command = three_ormore_interest)
button_calculate_interest = Button(root, text = "Multiply Interest", padx = 49, pady = 20, command = button_multiply)
button_equal = Button(root, text = "=", padx = 40, pady = 20, command = button_equal)
button_clear = Button(root, text = "Clear", padx = 126, pady = 20, command = button_clear)

#Put buttons on the screen
button_1.grid(row = 3, column=0)
button_2.grid(row = 3, column=1)
button_3.grid(row = 3, column=2)
button_4.grid(row = 2, column=0)
button_5.grid(row = 2, column=1)
button_6.grid(row = 2, column=2)
button_7.grid(row = 1, column=0)
button_8.grid(row = 1, column=1)
button_9.grid(row = 1, column=2)
button_0.grid(row = 4, column=0)
button_one_category.grid(row = 1, column = 4)
button_two_category.grid(row = 2, column = 4)
button_three_category.grid(row = 3, column = 4)
button_four_category.grid(row = 4, column = 4)
button_calculate_interest.grid(row = 4, column = 1, columnspan = 2)
button_clear.grid(row = 5, column = 0, columnspan = 3)
button_equal.grid(row = 5, column = 4)



root.mainloop()