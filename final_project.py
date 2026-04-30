#cybersecurity focused secure login page using tkinter for ui
import tkinter as tk
from tkinter import font

#create the main window
root = tk.Tk()
root.title("Secure Login Page")
root.geometry("300x200")
root.configure(background="black")

user_var = tk.StringVar()
pass_var = tk.StringVar()
newuser_var = tk.StringVar()
newpass_var = tk.StringVar()
verifypass_var = tk.StringVar()

def initial_page():
    def create_login_field():
        button.destroy()
        buttontwo.destroy()
        username_label = tk.Label(root, text="Username:", font = ())
        username_entry = tk.Entry(root, textvariable = user_var)
        username_label.pack()
        username_entry.pack()
        password_label = tk.Label(root, text="Password:")
        password_entry = tk.Entry(root,textvariable=pass_var,show="*")
        password_label.pack()
        password_entry.pack()
        back_button.pack()
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
        back_button.pack()
    def go_back():
        for widget in root.winfo_children():
            widget.destroy()
        initial_page()

    button = tk.Button(root, text = "Login", command = create_login_field)
    button.pack()
    buttontwo = tk.Button(root, text = "Create Account",command = create_account_field)
    buttontwo.pack()
    back_button = tk.Button(root, text = "Back", command = go_back)


def login():
    pass
def create_account():
    pass
def forgot_password():
    pass

#runs the program above
initial_page()
root.mainloop()