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
import re
from tkinter import ttk
import subprocess

# version 0.2.0

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

        process = subprocess.Popen(
            ["wget", "--progress=dot", url],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            bufsize=1,
            text=True
            )

        self.check_progress(process)

    def check_progress(self, process):
        line = process.stdout.readline()

        if line:
            line = line.strip()

            m = re.search(r"(\d+)%", line)
            if m:
                percent = m.group(1)
                self.status.config(text=f"Downloading... {percent}%")
            else:
                if "." in line:
                    dots = line.count(".")
                    self.status.config(text=f"Downloading... ({dots} dots)")
        
        if process.poll() is None:
            self.after(100, lambda: self.check_progress(process))
        else:
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
