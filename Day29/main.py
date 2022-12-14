from tkinter import *
from tkinter import messagebox

from password import getRandomPassword
from pyperclip import copy

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def handle_gen_password():
    password = getRandomPassword(numbers=5, symbols=5, letters=10)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_file(**kw):
    website = kw.get("website")
    email = kw.get("email")
    password = kw.get("password")
    data = f"{website} | {email} | {password}\n"

    with open("data.txt", "a") as f:
        f.write(data)


def handle_add_info():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not email or not password:
        messagebox.showerror(
            title="Error", message="Please dont't leave any fields empty!!"
        )
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"details: \n Email: {email}\n Password: {password}\n Is it ok to save?",
    )

    if is_ok:
        save_file(
            website=website,
            email=email,
            password=password,
        )

        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password-Manager")
window.config(padx=20, pady=20)

canvas_width = 200
canvas_height = 200
canvas = Canvas(width=canvas_width, height=canvas_height)
canvas.grid(row=0, column=1)
logo = PhotoImage(file="logo.png")
canvas.create_image(canvas_width / 2, canvas_height / 2, image=logo)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=56)
website_entry.grid(
    row=1,
    column=1,
    columnspan=2,
)
website_entry.focus()

email_label = Label(text="Email/username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=56)
email_entry.grid(
    row=2,
    column=1,
    columnspan=2,
)
email_entry.insert(0, "hanganda23@naver.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=40)
password_entry.grid(row=3, column=1)

password_gen_btn = Button(text="Generate", width=15, command=handle_gen_password)
password_gen_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=55, command=handle_add_info)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
