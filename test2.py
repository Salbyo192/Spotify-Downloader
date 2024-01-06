import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess

def download_music(option):
    url = url_entry.get()
    if url:
        if option == "Playlist":
            command = f"python -m zspotify -pl {url}"
        elif option == "Song":
            command = f"python -m zspotify -tr {url}"
        elif option == "Album":
            command = f"python -m zspotify -al {url}"

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
window.geometry("400x300")

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

# Create and place the Download buttons
playlist_button = ttk.Button(window, text="Download Playlist", command=lambda: download_music("Playlist"))
playlist_button.pack(pady=10)

song_button = ttk.Button(window, text="Download Song", command=lambda: download_music("Song"))
song_button.pack(pady=5)

album_button = ttk.Button(window, text="Download Album", command=lambda: download_music("Album"))
album_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
