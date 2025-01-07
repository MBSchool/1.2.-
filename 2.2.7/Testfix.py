import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog, messagebox


def do_command(command):
    global command_textbox, url_entry
    
    # Clear previous output
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()


    # Determine URL/IP, defaulting to localhost if empty
    url_val = url_entry.get().strip()
    if not url_val:
        url_val = "::1"  # IPv6 localhost
    
    try:
        # Construct the full command with the URL/IP
        full_command = f"{command} {url_val}"
        
        # Run the command and capture output
        p = subprocess.Popen(full_command, 
                             stdout=subprocess.PIPE, 
                             stderr=subprocess.PIPE, 
                             shell=True,
                             text=True)  # Added text=True for easier output handling


        # Get command results
        cmd_results, cmd_errors = p.communicate()
        
        # Insert results into text box
        command_textbox.insert(tk.END, cmd_results)
        
        # Check if there are any errors and highlight them
        if cmd_errors:
            command_textbox.insert(tk.END, "\nErrors:\n", "error")
            command_textbox.insert(tk.END, cmd_errors, "error")
        
    except Exception as e:
        # Handle any unexpected errors
        command_textbox.insert(tk.END, f"\nError executing command: {str(e)}")


def main():
    root = tk.Tk()
    root.title("Network Utility Tool")
    
    # Create main frame
    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(fill=tk.BOTH, expand=True)


    # URL/IP Entry
    url_text = tk.Label(frame, text="Enter URL or IP")
    url_text.pack()
    
    url_entry = tk.Entry(frame, width=40)
    url_entry.pack(pady=5)


    # Button Frame
    button_frame = tk.Frame(frame)
    button_frame.pack(pady=10)


    # Network Utility Buttons
    buttons = [
        ("Ping", "ping"),
        ("Trace Route", "tracert"),
        ("DNS lookup", "nslookup")
    ]


    for text, command in buttons:
        btn = tk.Button(button_frame, text=text, 
                        command=lambda cmd=command: do_command(cmd))
        btn.pack(side=tk.LEFT, padx=5)


    # Output Text Box
    command_textbox = tksc.ScrolledText(frame, height=10, width=100)
    command_textbox.pack(pady=10)
    
    # Add error tag configuration
    command_textbox.tag_config("error", foreground="red")


    root.mainloop()


if __name__ == "__main__":
    main()

