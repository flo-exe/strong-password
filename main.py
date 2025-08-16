# STRONG PASSWORD by flo-exe

# necessary built-in modules:
# > random - to allow for random number generation
# > Tkinter - for the GUI
# > string - for easy access to character type lists

import random
import tkinter as tk
import string

# grouping all lowercase, uppercase, digits, and only certain special characters
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*"

# PASSWORD GENERATION FUNCTION

def generate_password():
    # password length is the user input on the length slider
    length = length_slider.get()
    # the password gets the range of length variable and randomises it using random.choice
    password = "".join(random.choice(characters) for character in range(length))
    # producing the result_label widget
    result_label.config(text=password)
    copy_button.config(text="copy me")
    # showing the password result widget and copy button widget only after password generation
    if not copy_button.winfo_ismapped():
        result_label.pack(pady=1)
        copy_button.pack(pady=20)

# GUI CLIPBOARD COPY FUNCTION

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text"))
    root.update()
    copy_button.config(text="copied!")

# GUI WINDOW

root = tk.Tk()
root.title("Strong Password")
root.configure(bg="#122022")
# window dimensions and centering the window
WIDTH = 650
HEIGHT = 400
x = int((root.winfo_screenwidth() / 2) - (WIDTH / 2))
y = int((root.winfo_screenheight() / 2) - (HEIGHT / 2))
root.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')
root.resizable(False, False)
# favicon
favicon = tk.PhotoImage(file="icons/icon16.png")
root.iconphoto(True, favicon)

# GUI WIDGETS

# 1. generation button
generate_button = tk.Button(root, 
                        text="generate strong password >", 
                        command=generate_password,
                        font=("Terminal", 28),
                        fg="#e1ff60",
                        bg="#151a24",
                        activebackground="#090A0F",
                        activeforeground="#E5FF00",
                        relief="ridge")
generate_button.pack(pady=(50, 20))
# 2. user length entry
length_label = tk.Label(root, 
                        text="password length", 
                        font=("Terminal", 14), 
                        fg="#61aeb0", 
                        bg="#122022")
length_label.pack(pady=(0, 10))
length_slider = tk.Scale(root, 
                         from_=8, to=30, 
                         orient=tk.HORIZONTAL, 
                         length=200, 
                         bg="#122022", 
                         fg="#61aeb0",
                         activebackground="#1ad577",
                         troughcolor="#61aeb0")
length_slider.set(16) # (default value)
length_slider.pack(pady=(0,40))
# 3. results design - packed earlier under generate_password
result_label = tk.Label(root, 
                        text="",
                        font=("Terminal", 28),
                        fg="#53D9DB",
                        bg="#151a24")
# 4. copy to clipboard button design - packed earlier under generate_password
copy_button = tk.Button(root, 
                        text="copy me", 
                        command=copy_to_clipboard,
                        font=("Terminal", 16),
                        fg="#e1ff60",
                        bg="#151a24",
                        activebackground="#1ad577",
                        activeforeground="#000000",
                        relief="ridge"
                        )

# GUI EXECUTION

root.mainloop()