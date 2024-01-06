import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess

def read_token_from_file():
    try:
        with open("token", "r") as token_file:
            return token_file.read().strip()
    except FileNotFoundError:
        print("Token file not found.")
        return None

def download_music(option):
    if option in ["Playlist", "Song", "Album"]:
        url = url_entry.get()
        if url:
            command = ""
            if option == "Playlist":
                command = f"python -m zspotify -pl {url}"
            elif option == "Song":
                command = f"python -m zspotify -tr {url}"
            elif option == "Album":
                command = f"python -m zspotify -al {url}"

            # Read access token from the file
            access_token = read_token_from_file()

            if access_token:
                # Include the access token in the command
                command_with_token = f"{command} -t {access_token}"
                subprocess.run(command_with_token, shell=True)

                # Clear the URL entry
                url_entry.delete(0, tk.END)

                # Show the Finished window
                show_finished_window()
            else:
                messagebox.showerror("Error", "Access token not available.")
    elif option == "Spotify":
        query = query_entry.get()
        if query:
            command = f"python -m zspotify {query} search"

            # Read access token from the file
            access_token = read_token_from_file()

            if access_token:
                # Include the access token in the command
                command_with_token = f"{command} -t {access_token}"
                subprocess.run(command_with_token, shell=True)

                # Clear the Query entry
                query_entry.delete(0, tk.END)

                # Show the Finished window
                show_finished_window()
            else:
                messagebox.showerror("Error", "Access token not available.")

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
window.geometry("400x400")

# Style
style = ttk.Style()
style.configure("TButton", padding=5, font=('Helvetica', 12))
style.configure("TLabel", padding=5, font=('Helvetica', 12))

# Create and place the Label widget
label = ttk.Label(window, text="Insert Url")
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

# Create and place the Label widget
label = ttk.Label(window, text="Search Spotify")
label.pack(pady=5)

# Create and place the Search Query entry widget
query_entry = ttk.Entry(window, width=40)
query_entry.pack(pady=5)

# Create and place the Search Spotify button
spotify_button = ttk.Button(window, text="Search Spotify", command=lambda: download_music("Spotify"))
spotify_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
