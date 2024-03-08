"""This module runs a tkinter GUI for downloading GitHub Sub-Repositories and files inside them"""

import os
from tkinter import messagebox as mb
import customtkinter as ctk
from github import Github
from github.GithubException import UnknownObjectException

# Window Specifications
root = ctk.CTk()
root.title('GitHub Sub-Repositories Downloader')
root.geometry('600x600')
root.resizable(False, False)

# Download Logic
def download_it():
    """Downloads the contents from the limk provided"""

    try:
        repo_link = link.get().split('/')
        repo_link = f'{repo_link[3]}/{repo_link[4]}'
        Github().get_repo(repo_link)
    except UnknownObjectException:
        mb.showerror('ERROR', "The Link pasted doesn't consist any GitHub Repositories!")
    except IndexError:
        mb.showerror('ERROR', "The Link pasted doesn't consist any GitHub Repositories!")
    else:
        os.system(f'gitdir {link.get()}')
        mb.showinfo('SUCCESS', 'Download Succeeded!')

# Window Elements
ctk.CTkLabel(root, text='Paste the Link below').place(relx=0.5, rely=0.4, anchor='center')
link = ctk.StringVar()
textbox = ctk.CTkEntry(root, width=360, height=40, textvariable=link)
textbox.place(relx=0.2, rely=0.5)
button = ctk.CTkButton(root, height=30, text='Download', command=download_it)
button.place(relx=0.5, rely=0.7, anchor='center')

# For Fast Pasting
root.update()
textbox.focus()

# Repeat the Cycle
root.mainloop()
