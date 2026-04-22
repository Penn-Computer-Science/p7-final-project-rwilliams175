#cybersecurity focused secure login page using tkinter for ui
import tkinter as tk

#create the main window
root = tk.Tk()
root.title("Secure Login Page")
root.geometry("400x300")

name_var = tk.StringVar()

username_label = tk.Label(root, text="Username")
username_entry = tk.Entry(root, textvariable = name_var)
username_label.grid(row=0,column=0)
username_entry.grid(row=0,column=1)




def login():
    pass

#button = tk.Button(root, text = "Login", command = login)
#button.pack()

#runs the program above
root.mainloop()