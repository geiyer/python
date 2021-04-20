import  tkinter

def on_submit_click():
    localName = "Hello " + nameVariable.get()
    labelName.config(text=localName)

#main window
window = tkinter.Tk()
window.geometry("300x200")

#window title
window.title('Introduction to Python')

#Add Text Box
label = tkinter.Label(window, text="Enter Name")
nameVariable = tkinter.StringVar()
name_entry = tkinter.Entry(window, textvariable=nameVariable, width=20, bg="white")
button = tkinter.Button(window, text='Submit', width=25, command=on_submit_click)
button.pack()
# button.invoke()
labelName = tkinter.Label(window, text= "")

label.grid(row=0, column= 0 )
name_entry.grid(row=0, column= 1)
button.grid(row=2, column=0)
labelName.grid(row=3, column= 0 )
# window.bind('<Return>', on_submit_click)
#main loop: run
window.mainloop()

