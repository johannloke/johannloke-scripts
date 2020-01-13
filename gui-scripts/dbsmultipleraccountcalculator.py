from tkinter import *
import tkinter as tk

root = Tk()
root.title('DBS Multipler Account')
root.geometry("458x300")
root.configure(background = 'green')

#Define Numbers only in Entry
def only_numbers(char):
    return char.isdigit()

validation = root.register(only_numbers)
fields_checker = False

#Define calculate function
def calculate():


    if len(amount_box.get()) == 0 or len(categories_box.get()) == 0:
        inform_user_label = Label(root, text = "Please enter something!", font = ('Geometric sans-serif',20), fg = "red")
        inform_user_label.grid(row = 8, column = 0, columnspan = 2)
        amount_box.delete(0, END)
        categories_box.delete(0, END)
    else:
        amount = int(amount_box.get())
        categories = int(categories_box.get())
        fields_checker = True

        interest_rate = 0

        if categories == 1:
            if amount < 2000:
                interest_rate = 0.005
            elif 2000 <= amount < 2500:
                interest_rate = 0.0155
            elif 2500 <= amount < 5000:
                interest_rate = 0.0185
            elif 5000 <= amount < 15000:
                interest_rate = 0.019
            elif 15000 <= amount < 30000:
                interest_rate = 0.02
            else:
                interest_rate = 0.0208

        if categories == 2:        
            if amount < 2000:
                interest_rate = 0.005
            elif 2000 <= amount < 2500:
                interest_rate = 0.0180
            elif 2500 <= amount < 5000:
                interest_rate = 0.02
            elif 5000 <= amount < 15000:
                interest_rate = 0.022
            elif 15000 <= amount < 30000:
                interest_rate = 0.023
            else:
                interest_rate = 0.035

        if categories >= 3:
            if amount < 2000:
                interest_rate = 0.005
            elif 2000 <= amount < 2500:
                interest_rate = 0.02
            elif 2500 <= amount < 5000:
                interest_rate = 0.022
            elif 5000 <= amount < 15000:
                interest_rate = 0.024
            elif 15000 <= amount < 30000:
                interest_rate = 0.025
            else:
                interest_rate = 0.038  
        
        interest_earned = amount * interest_rate
        total_amount = interest_earned + amount

        global interest_label
        global total_amount_label

        interest_label = Label(root, text = str(interest_earned), font = ('Comic Sans MS',10))
        interest_label.grid(row = 3, column = 1, pady = (10,0))
        total_amount_label = Label(root, text = str(total_amount), font = ('Comic Sans MS',10))
        total_amount_label.grid(row = 4, column = 1, pady = (10,0))
        
        amount_box.delete(0, END)
        categories_box.delete(0, END)
    
#Define clear function
def clear():
    amount_box.delete(0, END)
    categories_box.delete(0, END)
    interest_label.destroy()
    total_amount_label.destroy()

#Create text box 
amount_box = Entry(root, width = 30, justify = RIGHT, validate = "key", validatecommand=(validation, '%S'))
amount_box.grid(row = 1, column = 1, pady = (10,0))
categories_box = Entry(root, width = 30, justify = RIGHT, validate = "key", validatecommand=(validation, '%S'))
categories_box.grid(row = 2, column = 1, pady = (10,0))

#Create labels
header_label = Label(root, text = "DBS Multiplier Savings Account")
header_label.grid(row = 0, column = 0, padx = 150, pady = (10,0), columnspan = 2)
amount_labels = Label(root, text = "Enter Amount in Account: ")
amount_labels.grid(row = 1, column = 0, pady = (10,0), sticky = W)
categories_label = Label(root, text = "Enter no. of categories (Min: 1, Max: 4)")
categories_label.grid(row = 2, column = 0, pady = (10,0), sticky = W)
interest_earned = Label(root, text = "Interest earned: ")
interest_earned.grid(row = 3, column = 0,  pady = (10,0), sticky = W)
total_amount_saved = Label(root, text = "Total Amount Saved: ")
total_amount_saved.grid(row = 4, column = 0, pady = (10,0), sticky = W)

#Create Button
calculate_button = Button(root, text = "Calculate", command = calculate, state = NORMAL)
calculate_button.grid(row = 5, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 100)
clear_button = Button(root, text = "Clear Boxes", command = clear)
clear_button.grid(row = 6, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 94)
root.mainloop()