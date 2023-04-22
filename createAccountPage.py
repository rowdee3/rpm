#Create Account Page

import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from databaseHandler import pwd_context

#general colour scheme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

#geometry of our window
width, height = 400, 600

#Main class for the Login Page.
class App(ctk.CTk):


    def confirmPasswordHashes(self):

        hashed = pwd_context.hash(self.passwordEntryWidget.get())
        
        if pwd_context.verify(self.passwordEntryConfirmWidget.get(), hashed):
            return 1
        else:
            return 0

    def createAccount(self):
        
         if self.confirmPasswordHashes() == 1:
            self.passwordEntryWidget.delete(first_index=0, last_index=tk.END)
            self.passwordEntryConfirmWidget.delete(first_index=0, last_index=tk.END)


    def __init__(self):
        super().__init__()
        self.geometry(f'{width}x{height}')
        self.title("RPM v0.0.1a")

        self.titleLabel = ctk.CTkLabel(self, text="rowdee's Password Manager")
        self.titleLabel.grid(row=0, column=2, pady=20, padx=2)

        self.subtitleLabel = ctk.CTkLabel(self, text="Create Account", font=('arial', 12))
        self.subtitleLabel.grid(row=1, column=2)
        
        self.usernameLabel = ctk.CTkLabel(self, text="Enter Username:")
        self.usernameLabel.grid(row=2, column=1, pady=20, padx=20)

        self.usernameEntryWidget = ctk.CTkEntry(self, placeholder_text="Username")
        self.usernameEntryWidget.grid(row=2, column=2, pady=20, padx=2)

        self.passwordLabel = ctk.CTkLabel(self, text="Enter Password:")
        self.passwordLabel.grid(row=3, column=1, pady=20, padx=20)

        self.passwordEntryWidget = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.passwordEntryWidget.grid(row=3, column=2, pady=20, padx=2)

        self.passwordConfirmLabel = ctk.CTkLabel(self, text="Enter Password Again:")
        self.passwordConfirmLabel.grid(row=4, column=1, pady=20, padx=20)

        self.passwordEntryConfirmWidget = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.passwordEntryConfirmWidget.grid(row=4, column=2, pady=20, padx=2)

        self.createAccount = ctk.CTkButton(self, text="Login", command=self.createAccount)
        self.createAccount.grid(row=5, column=2, pady=20, padx=20)

def runtime():
    app = App()
    app.mainloop()