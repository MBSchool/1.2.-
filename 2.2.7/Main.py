# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename




# Modify the do_command function:
#   to use the new button as needed

def do_command(command):
    global command_textbox, url_entry
    
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

# If url_entry is blank, use localhost IP address 
    url_val = url_entryhuh.get()
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"
        p = subprocess.Popen(command + ' ::1', stdout=subprocess.PIPE, stderr=subprocess.PIPE) #v2

    else:
        p = subprocess.Popen(command +  url_val , stdout=subprocess.PIPE, stderr=subprocess.PIPE) 

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)



root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

url_text = tk.Label(frame, text="Enter URL or IP")
url_text.pack()
url_val = tk.StringVar()
url_entryhuh = tk.Entry(frame, textvariable=url_val)
url_entryhuh.pack()

# Makes the command button pass it's name to a function using lambda
ping_btn = tk.Button(frame, text="Ping", command=lambda:do_command("ping"))
ping_btn.pack()

tracert_btn = tk.Button(frame, text="Trace Route", command=lambda:do_command("tracert"))
tracert_btn.pack()

dns_btn = tk.Button(frame, text="DNS lookup", command=lambda:do_command("nslookup"))
dns_btn.pack()

# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()
root.mainloop()
