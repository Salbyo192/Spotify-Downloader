import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests

def generate_token():
    client_id = client_id_entry.get()
    client_secret = client_secret_entry.get()

    if not client_id or not client_secret:
        messagebox.showerror("Error", "Please enter both Client ID and Client Secret.")
        return

    access_token = get_spotify_access_token(client_id, client_secret)

    if access_token:
        messagebox.showinfo("Success", "Access token successfully obtained and saved to 'token' file.")
    else:
        messagebox.showerror("Error", "Failed to obtain access token.")

def get_spotify_access_token(client_id, client_secret):
    token_url = "https://accounts.spotify.com/api/token"
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }

    response = requests.post(token_url, headers=headers, data=data)

    if response.status_code == 200:
        access_token = response.json().get("access_token")
        write_credentials_to_file(client_id, client_secret)
        write_token_to_file(access_token)
        return access_token
    else:
        print(f"Failed to retrieve access token. Status code: {response.status_code}")
        return None

def write_credentials_to_file(client_id, client_secret):
    with open("credentials.txt", "w") as credentials_file:
        credentials_file.write(f"Client ID: {client_id}\n")
        credentials_file.write(f"Client Secret: {client_secret}")

def write_token_to_file(access_token):
    with open("token", "w") as token_file:
        token_file.write(access_token)

# Create the main window
window = tk.Tk()
window.title("Spotify Access Token Generator")
window.geometry("300x200")

# Style
style = ttk.Style()
style.configure("TButton", padding=5, font=('Helvetica', 12))
style.configure("TLabel", padding=5, font=('Helvetica', 12))

# Create and place the Label widgets
client_id_label = ttk.Label(window, text="Client ID:")
client_id_label.pack(pady=5)

client_secret_label = ttk.Label(window, text="Client Secret:")
client_secret_label.pack(pady=5)

# Create and place the Entry widgets
client_id_entry = ttk.Entry(window, width=20)
client_id_entry.pack(pady=5)

client_secret_entry = ttk.Entry(window, width=20, show="*")  # Show asterisks for the secret
client_secret_entry.pack(pady=5)

# Create and place the Generate Token button
generate_button = ttk.Button(window, text="Generate Token", command=generate_token)
generate_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
