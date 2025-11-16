# WarpGet - Simple Download Manager GUI for wget
# Copyright (C) 2025 Sina Kiadaliri
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License v3 for more details.


import tkinter as tk
from tkinter import ttk
import os

# version 0.1.0

class WarpGetMainFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        ttk.Label(self, text="URL:", font=("Liberation Sans", 14)).grid(row=0, column=0, padx=5, pady=5)
        self.url_entry = ttk.Entry(self, width=50)
        self.url_entry.grid(row=0, column=1, padx=5, pady=5)
        self.download_btn = ttk.Button(self, text="Download", command=self.start_download)
        self.download_btn.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

        self.status = ttk.Label(self, text="", font=("Liberation Sans", 20))
        self.status.grid(row=2, column=0, columnspan=2, padx=5, pady=20)

    def start_download(self):
        self.status.config(text="Downloading...")
        url = self.url_entry.get()
        os.system(f"wget \"{url}\"")

        self.status.config(text="Download Complete!")

class WarpGet(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("500x300")
        self.title("WarpGet")

        self.config(bg="lightgray")

        mainframe = WarpGetMainFrame(self)
        mainframe.pack(pady=10)
        

if __name__ == "__main__":
    WarpGet().mainloop()
