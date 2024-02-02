import tkinter as tk

app = tk.Tk()
app.title("Python Desktop App")
app.geometry("400x300")

app.mainloop()

app = tk.Tk()
app.title("Python Desktop App")
app.geometry("400x300")

label = tk.Label(app, text="Enter your name:")
label.pack()

entry = tk.Entry(app)
entry.pack()

submit_button = tk.Button(app, text="Submit", )
submit_button.pack()

app.mainloop()

import sqlite3


def create_database():
    conn = sqlite3.connect("names.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS names (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )""")
    conn.commit()
    conn.close()


create_database()


def on_submit():
    name = entry.get()
    conn = sqlite3.connect("names.db")
    c = conn.cursor()

    c.execute("INSERT INTO names (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()


def update_listbox():
    conn = sqlite3.connect("names.db")
    c = conn.cursor()

    c.execute("SELECT * FROM names")
    rows = c.fetchall()

    listbox.delete(0, tk.END)
    for row in rows:
        listbox.insert(tk.END, row[1])

    conn.close()


listbox = tk.Listbox(app)
listbox.pack()

update_listbox()

