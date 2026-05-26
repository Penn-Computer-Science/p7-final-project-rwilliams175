#cybersecurity focused secure login page using tkinter for ui
import tkinter as tk
from tkinter import font
from tkinter import messagebox
import hashlib
import json
import os

#create the main window
root = tk.Tk()
root.title("Secure Login Page")
root.geometry("300x200")
root.configure(background="black")

USERS_FILE = "users.json"

fsociety = tk.PhotoImage(file="fsociety.png")

def load_user():
    if os.path.exists(USERS_FILE):
        file = open(USERS_FILE, "r")
        users = json.load(file)
        file.close()
        return users
    return {}
    
def save_users(users):
    file = open(USERS_FILE, "w")
    json.dump(users, file)
    file.close()

def hash_password(password):
    hashed = hashlib.sha256(password.encode())
    return hashed.hexdigest()


#Entry field input variables
user_var = tk.StringVar()
pass_var = tk.StringVar()
newuser_var = tk.StringVar()
newpass_var = tk.StringVar()
verifypass_var = tk.StringVar()

def initial_page():
    def create_login_field():
        button.destroy()
        buttontwo.destroy()
        username_label = tk.Label(root, text="Username:", font=('Lucida Sans Unicode', 8))
        username_entry = tk.Entry(root, textvariable = user_var)
        username_label.pack()
        username_entry.pack()
        password_label = tk.Label(root, text="Password:",font=('Lucida Sans Unicode', 8))
        password_entry = tk.Entry(root,textvariable=pass_var,show="*")
        password_label.pack()
        password_entry.pack()
        back_button.pack()
    def create_account_field():
        button.destroy()
        buttontwo.destroy()
        newuser_label = tk.Label(root, text="Create Username:",font=('Lucida Sans Unicode', 8))
        newuser_entry = tk.Entry(root, textvariable = newuser_var)
        newpass_label = tk.Label(root, text = "Create Password:",font=('Lucida Sans Unicode', 8))
        newpass_entry = tk.Entry(root, textvariable = newpass_var, show = "*")
        verifypass_label = tk.Label(root, text = "Verify Password:",font=('Lucida Sans Unicode', 8))
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

    button = tk.Button(root, text = "Login", command = create_login_field,font=('Lucida Sans Unicode', 8))
    button.pack()
    buttontwo = tk.Button(root, text = "Create Account",command = create_account_field,font=('Lucida Sans Unicode', 8))
    buttontwo.pack()
    back_button = tk.Button(root, text = "Back", command = go_back,font=('Lucida Sans Unicode', 8))


def login():
    username = user_var.get()
    password = pass_var.get()

    if username == "" or password == "":
        messagebox.showwarning("Login","Please enter a username or password")
        return
    users = load_user()
    if username not in users:
        messagebox.showerror("Login","Username not found")
        return
    messagebox.showinfo("Login","Welcome ", + username + "!")
    user_var.set("")
    pass_var.set("")
    landing_page()

def create_account():
    username = newuser_var.get()
    password = newpass_var.get()
    verify = verifypass_var.get()

    if username == "" or password == "" or verify == "":
        messagebox.showwarning("Create Account", "All fields must filled out")
        return
    
    if verify == password:
        messagebox.showerror("Create Account", "Passwords must match")
        return
    
    users = load_user

    if username in users:
        messagebox.showerror("Create Account", "Username already taken")
        return
    
    users[username] = hash_password(password)
    messagebox.showinfo("Create Account", "Account created successfully. You can now log in.")
    newuser_var.set("")
    newpass_var.set("")
    verifypass_var.set("")

    for widget in root.winfo_children():
        widget.destroy()
        initial_page()

def forgot_password():
    pass
def landing_page():
    tk.Label(image = fsociety).pack()



#runs the program above
initial_page()
root.mainloop()