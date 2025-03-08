from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbol = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbol + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_enter.get().lower()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="dont leave any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Read the data Through Load method
                data = json.load(data_file)    # print(data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Write the data(Update) to the json data
                json.dump(data, data_file, indent=3)
        else:
            # Update the new_data(dictionary) to the data(file name which is read)
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Write the data(Update) to the json data
                json.dump(data, data_file, indent=3)
        finally:
            website_enter.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- find Password ------------------------------- #
def find_password():
    website = website_enter.get().lower()
    try:
        with open("data.json")as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="no data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error", message="no detail file found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password manager")
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", fg="red")
website_label.grid(row=1, column=0)
email_label = Label(text="email:", fg="red")
email_label.grid(row=2, column=0)
password_label = Label(text="password:", fg="red")
password_label.grid(row=3, column=0)

# Entries
website_enter = Entry(width=21)
website_enter.grid(row=1, column=1)
website_enter.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "abhi@email.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Button
search_button = Button(text="search", width=13, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="generate password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
