import  tkinter


def on_button_click():
    label.config(text="Nice choice")


#main window
window = tkinter.Tk()


#window title
window.title('Introduction to Python')
# Add all controls here



# #Add Checkbox
var1 = tkinter.IntVar()
check = tkinter.Checkbutton(window, text="CIS", variable=var1).grid(row=0)

var2 = tkinter.IntVar()
check = tkinter.Checkbutton(window, text="BIS", variable=var2).grid(row=1)

# #Add Submit Buttons
button = tkinter.Button(window, text='Choose', width=25, command=on_button_click)
button.grid(row=3)
exit_button = tkinter.Button(window, text='Exit', width=25, command=window.destroy)
exit_button.grid(row=5)

# #Add Labels
label = tkinter.Label(window, text="No Selection Made")
label.grid(row=4)

#main loop: run
window.mainloop()

