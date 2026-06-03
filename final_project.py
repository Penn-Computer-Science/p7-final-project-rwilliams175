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
root.geometry("400x350")
root.configure(background="black")
root.resizable(False, False)

USERS_FILE = "users.json"

fsociety = tk.PhotoImage(file="fsociety.png")

BG = "black"
WIDGET = "#222222"
GREEN = "#00ff00"
WHITE = "white"
FONT = ('Courier New', 10)
FONT_LG = ('Courier New', 14, 'bold')

def load_user():
    if os.path.exists(USERS_FILE):
        file = open(USERS_FILE, "r")
        contents = file.read()
        file.close()
        if contents == "":
            return {}
        users = json.loads(contents)
        return users
    return {}
    
def save_users(users):
    file = open(USERS_FILE, "w")
    json.dump(users, file)
    file.close()

def hash_password(password):
    hashed = hashlib.sha256(password.encode())
    return hashed.hexdigest()

def make_button(parent, text, command):
    return tk.Button(parent, text=text, command=command, font=FONT, bg=WIDGET, fg = GREEN, activebackground=GREEN,activeforeground="black",relief="flat",cursor="hand2", width=20, pady=4)

def make_label(parent,text):
    return tk.Label(parent, text = text, font = FONT, bg = BG, fg = WHITE)

def make_entry(parent,textvariable,show=None):
    if show:
        return tk.Entry(parent, textvariable=textvariable, show=show,font=FONT, bg=WIDGET, fg=WHITE,insertbackground=WHITE, relief="flat", width=22)
    return tk.Entry(parent, textvariable=textvariable,font=FONT, bg=WIDGET, fg=WHITE,insertbackground=WHITE, relief="flat", width=22)

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
 
        title = tk.Label(root, text="-- LOGIN --", font=FONT_LG, bg=BG, fg=GREEN)
        title.grid(row=0, column=0, columnspan=2, pady=(20, 10))
 
        make_label(root, "Username:").grid(row=1, column=0, padx=10, pady=6, sticky="e")
        make_entry(root, user_var).grid(row=1, column=1, padx=10, pady=6)
 
        make_label(root, "Password:").grid(row=2, column=0, padx=10, pady=6, sticky="e")
        make_entry(root, pass_var, show="*").grid(row=2, column=1, padx=10, pady=6)
 
        make_button(root, "Login", login).grid(row=3, column=0, columnspan=2, pady=(10, 2))
        back_button.grid(row=4, column=0, columnspan=2, pady=2)
        root.bind("<Return>", login_keypress)
    def create_account_field():
        button.destroy()
        buttontwo.destroy()
 
        title = tk.Label(root, text="   CREATE ACCOUNT   ", font=FONT_LG, bg=BG, fg=GREEN)
        title.grid(row=0, column=0, columnspan=2, pady=(20, 10))
 
        make_label(root, "Username:").grid(row=1, column=0, padx=10, pady=6, sticky="e")
        make_entry(root, newuser_var).grid(row=1, column=1, padx=10, pady=6)
 
        make_label(root, "Password:").grid(row=2, column=0, padx=10, pady=6, sticky="e")
        make_entry(root, newpass_var, show="*").grid(row=2, column=1, padx=10, pady=6)
 
        make_label(root, "Verify:").grid(row=3, column=0, padx=10, pady=6, sticky="e")
        make_entry(root, verifypass_var, show="*").grid(row=3, column=1, padx=10, pady=6)
 
        make_button(root, "Create Account", create_account).grid(row=4, column=0, columnspan=2, pady=(10, 2))
        back_button.grid(row=5, column=0, columnspan=2, pady=2)
        root.bind("<Return>", create_account_keypress)
    def go_back():
        root.unbind("<Return>")
        for widget in root.winfo_children():
            widget.destroy()
        initial_page()

    title = tk.Label(root, text="  SECURE LOGIN  ", font=FONT_LG, bg=BG, fg=GREEN)
    title.grid(row=0, column=0, columnspan=2, pady=(40, 20))
 
    button = make_button(root, "Login", create_login_field)
    button.grid(row=1, column=0, columnspan=2, pady=6)
 
    buttontwo = make_button(root, "Create Account", create_account_field)
    buttontwo.grid(row=2, column=0, columnspan=2, pady=6)
 
    back_button = make_button(root, "Back", go_back)
 
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)


def login_keypress(event):
    login()

def create_account_keypress(event):
    create_account()


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
    if users[username] != hash_password(password):
        messagebox.showerror("Login", "Incorrect password")
        return
    messagebox.showinfo("Login","Welcome, " + username + "!")
    user_var.set("")
    pass_var.set("")
    root.unbind("<Return>")
    landing_page()

def create_account():
    username = newuser_var.get()
    password = newpass_var.get()
    verify = verifypass_var.get()

    if username == "" or password == "" or verify == "":
        messagebox.showwarning("Create Account", "All fields must filled out")
        return
    
    if verify != password:
        messagebox.showerror("Create Account", "Passwords must match")
        return
    
    users = load_user()

    if username in users:
        messagebox.showerror("Create Account", "Username already taken")
        return
    
    users[username] = hash_password(password)
    save_users(users)
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
    for widget in root.winfo_children():
        widget.destroy()
    image_label = tk.Label(root, image=fsociety, bg=BG)
    image_label.image = fsociety
    image_label.pack(expand=True)



#runs the program above
initial_page()
root.mainloop()