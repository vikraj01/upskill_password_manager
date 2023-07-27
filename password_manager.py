from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("Password Manager")
root.geometry("500x400")
root.minsize(600, 400)
root.maxsize(600, 400) 

frame = Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.50, rely=0.50, relwidth=0.98, relheight=0.45, anchor="n")

# Create Database
conn = sqlite3.connect("passmanager.db")
cursor = conn.cursor()

# Create table
cursor.execute("""CREATE TABLE IF NOT EXISTS manager (
                   app_name text,
                   url text,
                   email_id text,
                   password text
                )""")

# Commit changes
conn.commit()
# Close connection
conn.close()

# Create Table Structure for displaying data

# Create submit function for database
def submit():
    # Connect to database
    conn = sqlite3.connect("passmanager.db")
    cursor = conn.cursor()

    # Insert Into Table
    if app_name_entry.get() != "" and url_entry.get() != "" and email_id_entry.get() != "" and password_entry.get() != "":
        cursor.execute("INSERT INTO manager VALUES (:app_name, :url, :email_id, :password)",
                       {
                           'app_name': app_name_entry.get(),
                           'url': url_entry.get(),
                           'email_id': email_id_entry.get(),
                           'password': password_entry.get()
                       }
                       )
        # Commit changes
        conn.commit()
        # Close connection
        conn.close()
        # Message box
        messagebox.showinfo("Info", "Record Added in Database!")

        # After data entry clear the text boxes
        app_name_entry.delete(0, END)
        url_entry.delete(0, END)
        email_id_entry.delete(0, END)
        password_entry.delete(0, END)

    else:
        messagebox.showinfo("Alert", "Please fill all details!")
        conn.close()

# Create Query Function
def query():
    # set button text
    query_btn.configure(text="Hide Records", command=hide)
    # Connect to database
    conn = sqlite3.connect("passmanager.db")
    cursor = conn.cursor()

    # Query the database
    cursor.execute("SELECT *, oid FROM manager")
    records = cursor.fetchall()

    p_records = ""
    for record in records:
        p_records += f"{record[4]} {record[0]} {record[1]} {record[2]} {record[3]}\n"

    query_label['text'] = p_records
    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

# Create Function to Delete A Record
def delete():
    # Connect to database
    conn = sqlite3.connect("passmanager.db")
    cursor = conn.cursor()

    # Query the database
    t = delete_id_entry.get()
    if t != "":
        cursor.execute("DELETE FROM manager where oid = ?", (t,))
        delete_id_entry.delete(0, END)
        messagebox.showinfo("Alert", f"Record {t} Deleted")
    else:
        messagebox.showinfo("Alert", "Please enter record id to delete!")

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

# Create Function to Update A Record
def update():
    t = update_id_entry.get()
    if t != "":
        global edit
        edit = Tk()
        edit.title("Update Record")
        edit.geometry("500x400")
        edit.minsize(450, 300)
        edit.maxsize(450, 300)

        # Global variables
        global app_name_entry_edit, url_entry_edit, email_id_entry_edit, password_entry_edit

        # Create Text Boxes
        app_name_entry_edit = Entry(edit, width=30)
        app_name_entry_edit.grid(row=0, column=1, padx=20)
        url_entry_edit = Entry(edit, width=30)
        url_entry_edit.grid(row=1, column=1, padx=20)
        email_id_entry_edit = Entry(edit, width=30)
        email_id_entry_edit.grid(row=2, column=1, padx=20)
        password_entry_edit = Entry(edit, width=30)
        password_entry_edit.grid(row=3, column=1, padx=20)

        # Create Text Box Labels
        app_name_label_edit = Label(edit, text="Application Name:")
        app_name_label_edit.grid(row=0, column=0)
        url_label_edit = Label(edit, text="URL:")
        url_label_edit.grid(row=1, column=0)
        email_id_label_edit = Label(edit, text="Email Id:")
        email_id_label_edit.grid(row=2, column=0)
        password_label_edit = Label(edit, text="Password:")
        password_label_edit.grid(row=3, column=0)

        # Create Save Button
        submit_btn_edit = Button(edit, text="Save Record", command=change)
        submit_btn_edit.grid(row=4, column=0, columnspan=2, pady=5, padx=15, ipadx=135)

        # Connect to database
        conn = sqlite3.connect("passmanager.db")
        cursor = conn.cursor()

        # Query the database
        cursor.execute("SELECT * FROM manager where oid = ?", (t,))
        records = cursor.fetchall()

        for record in records:
            app_name_entry_edit.insert(0, record[0])
            url_entry_edit.insert(0, record[1])
            email_id_entry_edit.insert(0, record[2])
            password_entry_edit.insert(0, record[3])

        # Commit changes
        conn.commit()

        # Close connection
        conn.close()

    else:
        messagebox.showinfo("Alert", "Please enter record id to update!")

# Create function to save updated records
def change():
    # Connect to database
    conn = sqlite3.connect("passmanager.db")
    cursor = conn.cursor()

    # Insert Into Table
    if app_name_entry_edit.get() != "" and url_entry_edit.get() != "" and email_id_entry_edit.get() != "" and password_entry_edit.get() != "":
        cursor.execute("""UPDATE manager SET 
                            app_name = :app_name,
                            url = :url,
                            email_id = :email_id,
                            password = :password

                            WHERE oid = :oid""",
                       {
                           'app_name': app_name_entry_edit.get(),
                           'url': url_entry_edit.get(),
                           'email_id': email_id_entry_edit.get(),
                           'password': password_entry_edit.get(),
                           'oid': update_id_entry.get()
                       }
                       )
        # Commit changes
        conn.commit()
        # Close connection
        conn.close()
        # Message box
        messagebox.showinfo("Info", "Record Updated in Database!")

        # After data entry clear the text box and destroy the secondary window
        update_id_entry.delete(0, END)
        edit.destroy()

    else:
        messagebox.showinfo("Alert", "Please fill all details!")
        conn.close()

# Create Function to Hide Records
def hide():
    query_label['text'] = ""
    query_btn.configure(text="Show Records", command=query)


# Create Text Boxes
app_name_entry = Entry(root, width=30)
app_name_entry.grid(row=0, column=1, padx=20)
url_entry = Entry(root, width=30)
url_entry.grid(row=1, column=1, padx=20)
email_id_entry = Entry(root, width=30)
email_id_entry.grid(row=2, column=1, padx=20)
password_entry = Entry(root, width=30)
password_entry.grid(row=3, column=1, padx=20)
delete_id_entry = Entry(root, width=20)
delete_id_entry.grid(row=6, column=1, padx=20)
update_id_entry = Entry(root, width=20)
update_id_entry.grid(row=7, column=1, padx=20)

# Create Text Box Labels
app_name_label = Label(root, text="Application Name:")
app_name_label.grid(row=0, column=0)
url_label = Label(root, text="URL:")
url_label.grid(row=1, column=0)
email_id_label = Label(root, text="Email Id:")
email_id_label.grid(row=2, column=0)
password_label = Label(root, text="Password:")
password_label.grid(row=3, column=0)

# Create Submit Button
submit_btn = Button(root, text="Add Record", command=submit)
submit_btn.grid(row=5, column=0, pady=5, padx=15, ipadx=35)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=5, column=1, pady=5, padx=5, ipadx=35)

# Create a Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=6, column=0, ipadx=30)

# Create a Update Button
update_btn = Button(root, text="Update Record", command=update)
update_btn.grid(row=7, column=0, ipadx=30)

# Create a Label to show responses
query_label = Label(frame, anchor="nw", justify="left")
query_label.place(relwidth=1, relheight=1)

def main():
    root.mainloop()

if __name__ == '__main__':
    main()

# root.mainloop()
