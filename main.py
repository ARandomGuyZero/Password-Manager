"""
Password Manager

Author: Alan
Date: September 16th 2024

This password manager project gets the input of a certain website, the email and the password.
It saves this information to a data.txt file, where it can be accessed to read.
It can also generate a password and copy it to the clipboard.
"""

from random import randint
from tkinter import *
from tkinter import messagebox
from pyperclip import copy
from random import choice, shuffle

# Lists of characters to be used in the password
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    """
    Generates a password using letters, symbols and numbers and copies it to the clipboard
    """
    # Generate the required number of letters and add them to the password list
    letter_list = [choice(letters) for _ in range(randint(8, 10))]

    # Generate the required number of symbols and add them to the password list
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]

    # Generate the required number of numbers and add them to the password list
    number_list = [choice(numbers) for _ in range(randint(2, 4))]

    # Append all lists into one
    list_pass = letter_list + symbol_list + number_list

    # Randomly shuffle the characters in the password list to enhance security
    shuffle(list_pass)

    # Convert the list of characters into a string to form the final password
    password = ''.join(list_pass)

    # Copies the password to the clipboard
    copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, f"{password}")

def save():
    """
    Saves the data input into the data.txt file
    """

    # Get the data from the entry widgets
    website_name = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # If all fields are not empty, it'll ask the user to save the data
    if len(website_name) and len(email) and len(password):

        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs this ok to save?")

        if is_ok:
            with open("data.txt", mode="a") as data:
                # Write the data
                data.write(f"{website_name} | {email} | {password}\n")

                # Delete the data
                website_entry.delete(0, END)
                password_entry.delete(0, END)

    # Asks the user to fill all the fields
    else:
        messagebox.showinfo(title="Missing data!", message="Sorry, make sure you didn't leave any field empty!")

# New window titled Password Manager
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# New image
logo_img = PhotoImage(file="logo.png")

# Create new canvas for our image
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

# Website entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
website_entry.focus()

# Email label
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

# Email entry
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
email_entry.insert(0, "testing@email.com")

# Password label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Password entry
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="ew")

# Generate password button
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

# Generate password button
password_button = Button(text="Add", width=36, command=save)
password_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()