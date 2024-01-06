import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess

def download_music():
    url = url_entry.get()
    if url:
        command = f"python -m zspotify -pl {url}"
        subprocess.run(command, shell=True)
        
        # Clear the URL entry
        url_entry.delete(0, tk.END)
        
        # Show the Finished window
        show_finished_window()

def show_finished_window():
    finished_window = tk.Toplevel(window)
    finished_window.title("Finished!")

    label_finished = ttk.Label(finished_window, text="Finished!", font=('Helvetica', 16, 'bold'))
    label_finished.pack(pady=10)

    ok_button = ttk.Button(finished_window, text="OK", command=finished_window.destroy)
    ok_button.pack(pady=10)

# Create the main window
window = tk.Tk()
window.title("Spotify Downloader")
window.geometry("400x200")

# Style
style = ttk.Style()
style.configure("TButton", padding=5, font=('Helvetica', 12))
style.configure("TLabel", padding=5, font=('Helvetica', 12))

# Create and place the Label widget
label = ttk.Label(window, text="Insert Url Here")
label.pack(pady=5)

# Create and place the URL entry widget
url_entry = ttk.Entry(window, width=40)
url_entry.pack(pady=5)

# Create and place the Download button
download_button = ttk.Button(window, text="Download", command=download_music)
download_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
