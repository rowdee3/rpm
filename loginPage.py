#The login page.

#Import Libraries
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

#general colour scheme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

#geometry of our window
width, height = 400, 600

#Main class for the Login Page.
class App(ctk.CTk):
    
    def loginHandler(self):
        pass

    def createAccount(self):
        pass

    def __init__(self):
        super().__init__()
        self.geometry(f'{width}x{height}')
        self.title("RPM v0.0.1a")

        self.titleLabel = ctk.CTkLabel(self, text="rowdee's Password Manager")
        self.titleLabel.grid(row=0, column=2, pady=20, padx=2)

        self.subtitleLabel = ctk.CTkLabel(self, text="v0.0.1a", font=('arial', 12))
        self.subtitleLabel.grid(row=1, column=2)
        
        self.usernameLabel = ctk.CTkLabel(self, text="Username:")
        self.usernameLabel.grid(row=2, column=1, pady=20, padx=20)

        self.usernameEntryWidget = ctk.CTkEntry(self, placeholder_text="Username")
        self.usernameEntryWidget.grid(row=2, column=2, pady=20, padx=2)

        self.passwordLabel = ctk.CTkLabel(self, text="Password:")
        self.passwordLabel.grid(row=3, column=1, pady=20, padx=20)

        self.passwordEntryWidget = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.passwordEntryWidget.grid(row=3, column=2, pady=20, padx=2)

        self.loginButton = ctk.CTkButton(self, text="Login", command=self.loginHandler)
        self.loginButton.grid(row=4, column=2, pady=20, padx=20)

        self.createAccountButton = ctk.CTkButton(self, text="Create Account", command=self.createAccount)
        self.createAccountButton.grid(row=5, column=2, pady=20, padx=20)


if __name__ == '__main__':
    app = App()
    app.mainloop()