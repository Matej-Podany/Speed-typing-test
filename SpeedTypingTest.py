# Project Speed typing test by team STT (including Matej Podany; 221344) version 1.0

import tkinter as tk
import random
from tkinter import ttk
import time

# main window = win1
win1 = tk.Tk()

# name of win1
win1.title('Speed typing test')

# settings for the window
win1.resizable(False, False)

# opening data
file_data = open("data.txt", "r")
data = file_data.readlines()

# creating confirmation
confirmation = tk.StringVar()

# average, Wwords etc.
average = 0
Wwords = 0
average_value = 0
result = 0
beginning_time = 0

# test function
def start_test():
    
    # deleting previouse text in field or mistaker
    field.delete(0, tk.END)
    mistaker.grid_forget()
    
    # first start
    global first_start
    if average == Wwords == result == 0:
        first_start = 1
    
    # choosing sentence
    global sentence
    random_number = random.randrange(0, len(data))
    sentence = data[random_number]
    sentence = sentence.strip()
    
    # number of words in sentence
    counter = 1
    global words_in_sentence
    for i in sentence:
        if i == " ":
            counter += 1
    words_in_sentence = counter
  
    # printing text
    text.configure(text=sentence)
    
    # focusing cursor
    field.focus()
    
    # timer
    global starting_time
    starting_time = time.perf_counter()

# check function
def check_sentence():
    
    # collecting informations
    global average_value
    global result
    average_holder = average_value
    result_holder = result
    
    # timing
    ending_time = time.perf_counter()
    result = ending_time - starting_time
    timer.configure(text=result)
    global first_start
    while 1:
        if first_start == 1:
            timer.configure(foreground="green")
            first_start = 0
            break
        if result <= result_holder:
            timer.configure(foreground="green")
            break
        if result > result_holder:
            timer.configure(foreground="red")
            break
    
    # statistics
    average_value = words_in_sentence / (result / 60)
    Wwords = words_in_sentence
    
    # mistake or not
    if confirmation.get()!=sentence:
        mistaker.grid(column=2, row = 3)
    
    if confirmation.get()==sentence:
        average_label.configure(text=average_value)
        words_label.configure(text=Wwords)
        
        if average_value >= average_holder:
            average_label.configure(foreground="green")
        if average_value < average_holder:
            average_label.configure(foreground="red")
        
# text in win1
ttk.Label(win1, text="Welcome at speed typing test! Remember that you have to write the text correctly!").grid(column=0, row = 0)
ttk.Label(win1, text="Your statiscics will be visible after you finish your sentence.").grid(column=1, row = 0)
ttk.Label(win1, text="After you click at START! button, your cursor will be automatically in writing box.").grid(column=0, row = 1)
ttk.Label(win1, text="When you are done with your writing, click on the Check button.").grid(column=0, row = 2)

# start button
start = ttk.Button(win1, text="START!", command=start_test)
start.grid(column=2, row = 1)

# check button
check = ttk.Button(win1, text="Check", command=check_sentence)
check.grid(column=2, row = 2)

# mistaker
mistaker = ttk.Label(win1, text="MISTAKE!", foreground="red")

# text to be written
text = ttk.Label(win1, text="Your text will be here", foreground="red", relief="ridge")
text.grid(column=1, row = 1)

# timer
timer = ttk.Label(win1, text=beginning_time)
timer.grid(column=1, row = 3)

# writing field
field_w = 70
field = ttk.Entry(win1, width=field_w, textvariable=confirmation)
field.grid(column=1, row = 2)

# statistics text
ttk.Label(win1, text="Your writing time [s]:").grid(column=0, row = 3)
ttk.Label(win1, text="Typing speed [w/m]:").grid(column=0, row = 4)
ttk.Label(win1, text="Number of written words [-]:").grid(column=0, row = 5)

# statistics field
average_label = ttk.Label(win1, text=average)
average_label.grid(column=1, row = 4)
words_label = ttk.Label(win1, text=Wwords)
words_label.grid(column=1, row = 5)

win1.mainloop()