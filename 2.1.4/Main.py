#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window

root = tk.Tk()
root.title('Authorization')
root.wm_geometry("150x200")


# create empty frame

frame_login = tk.Frame(root)
frame_login.grid()

# Setting up username field

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5, padx=10)

# Setting up password field 

lbl_password = tk.Label(frame_login,text="Password:",)
lbl_password.pack()

ent_password = tk.Entry(frame_login, bd=3, show='*')
ent_password.pack(pady=5, padx=10)

# Password button

btn_login = tk.Button(frame_login, text='Login',)
btn_login.pack()



# Mainloop end

root.mainloop()