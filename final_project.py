#cybersecurity focused secure login page using tkinter for ui
import tkinter as tk

#create the main window
root = tk.Tk()
root.title("Secure Login Page")
root.geometry("400x300")

user_var = tk.StringVar()
pass_var = tk.StringVar()
newuser_var = tk.StringVar()
newpass_var = tk.StringVar()
verifypass_var = tk.StringVar()

def create_entry_field():
    button.destroy()
    buttontwo.destroy()
    username_label = tk.Label(root, text="Username:")
    username_entry = tk.Entry(root, textvariable = user_var)
    username_label.pack()
    username_entry.pack()
    password_label = tk.Label(root, text="Password:")
    password_entry = tk.Entry(root,textvariable=pass_var,show="*")
    password_label.pack()
    password_entry.pack()
def create_account_field():
    button.destroy()
    buttontwo.destroy()
    newuser_label = tk.Label(root, text="Create Username:")
    newuser_entry = tk.Entry(root, textvariable = newuser_var)
    newpass_label = tk.Label(root, text = "Create Password:")
    newpass_entry = tk.Entry(root, textvariable = newpass_var, show = "*")
    verifypass_label = tk.Label(root, text = "Verify Password:")
    verifypass_entry = tk.Entry(root, textvariable = verifypass_var, show = "*")
    newuser_label.pack()
    newuser_entry.pack()
    newpass_label.pack()
    newpass_entry.pack()
    verifypass_label.pack()
    verifypass_entry.pack()

button = tk.Button(root, text = "Login", command = create_entry_field)
button.pack()
buttontwo = tk.Button(root, text = "Create Account",command = create_account_field)
buttontwo.pack()

def login():
    pass
def create_account():
    pass
def forgot_password():
    pass

#runs the program above
root.mainloop()