# Downloading the Required Packages
import os, platform
os.system('pip install customtkinter gitdir PyGithub')

# Importing the Necessary Libraries
import customtkinter as ctk
from github import Github
from tkinter import messagebox as mb
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

# Window Specifications
root = ctk.CTk()
root.title('GitHub Sub-Repositories Downloader')
root.geometry('600x600')
root.resizable(False, False)

# Download Logic
def downloadIt():
    try:
        repo_link = link.get().split('/')
        repo_link = f'{repo_link[3]}/{repo_link[4]}'
        Github().get_repo(repo_link)
    except:
        mb.showerror('ERROR', "The Link pasted doesn't consist any GitHub Repositories. Make sure the link is valid and try again!")
    else:
        path = ctk.filedialog.askdirectory()
        os.system(f'gitdir --output_dir {path} {link.get()}')
        mb.showinfo('SUCCESS', 'Download Succeeded!')

# Window Elements
ctk.CTkLabel(root, text='Paste the Link below').place(relx=0.5, rely=0.4, anchor='center')
link = ctk.StringVar()
textbox = ctk.CTkEntry(root, width=360, height=40, textvariable=link)
textbox.place(relx=0.2, rely=0.5)
ctk.CTkButton(root, height=30, text='Download', command=downloadIt).place(relx=0.5, rely=0.7, anchor='center')

# For Fast Pasting
root.update()
textbox.focus()

# Repeat the Cycle
root.mainloop()