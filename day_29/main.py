import tkinter as tk
from tkinter import messagebox
from pswrd_generator import PasswordGenerator
import pyperclip


LOGO_PATH = '21_30/day_29/logo.png'
DEFAULT_EMAIL = 'my@email.com'
DATA_FILE = '21_30/day_29/data.txt'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
pass_gen = PasswordGenerator()

def create_password():
    password_entry.delete(0, tk.END)
    password = pass_gen.generate_password()
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pswd():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    
    """
    messagebox.showinfo(title='Added!',
                           message=f'Data for {website} added succesfully!')
    """
    
    if len(website) < 1 or len(password) < 0:
        messagebox.showinfo(title='Missed data!',
                            message='Please enter Website and Password!')
    
    else:
        msg = f'Details entered:\nEmail: {email}\nPassword: {password}\nSave it?'
        
        is_ok = messagebox.askokcancel(title=website, message=msg)
        
        if is_ok:
            with open(DATA_FILE, 'a+') as f:
                f.write(f'{website} | {email} | {password}\n')
            
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            
        
# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title('Password Manager')
window.config(padx=40,
              pady=40)


# add picture
canvas = tk.Canvas(width=200,
                   height=200,
                   highlightthickness=0)
logo_image = tk.PhotoImage(file=LOGO_PATH)
canvas.create_image(100,100, image=logo_image)
canvas.grid(column=1,
            row=0)


# add labels
website_label = tk.Label(text='Website:')
email_label = tk.Label(text='Email/Username:')
password_label = tk.Label(text='Password:')

website_label.grid(column=0,
                   row=1)
email_label.grid(column=0,
                 row=2)
password_label.grid(column=0,
                    row=3)


# add entries
website_entry = tk.Entry(width=46)
email_entry = tk.Entry(width=46)
password_entry = tk.Entry(width=28)


website_entry.grid(column=1,
                   row=1,
                   columnspan=2)
website_entry.focus()
email_entry.grid(column=1,
                 row=2,
                 columnspan=2)
email_entry.insert(tk.END, DEFAULT_EMAIL)
password_entry.grid(column=1,
                    row=3)



# add buttons
generate_pass_button = tk.Button(text='Generate Password',
                                 width=14,
                                 command=create_password)
add_button = tk.Button(text='Add',
                       width=43,
                       command=save_pswd)
generate_pass_button.grid(column=2,
                          row=3)
add_button.grid(column=1,
                row=4,
                columnspan=2)


window.mainloop()