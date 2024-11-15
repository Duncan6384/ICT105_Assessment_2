import tkinter as tk
from tkinter import messagebox

from database_setup import is_unique_student_id, save_student_to_database

def register_student_ui():
    def register():
        student_id = entry_id.get()
        name = entry_name.get()
        email = entry_email.get()
        if is_unique_student_id(student_id):
            student = {"student_id": student_id, "name": name, "email": email}
            save_student_to_database(student)
            messagebox.showinfo("Success", "Student registered successfully!")
            clear_fields()
        else:
            messagebox.showerror("Error", "Student ID already exists.")

    def clear_fields():
        entry_id.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)

    window = tk.Tk()
    window.title("Student Registration")

    tk.Label(window, text="Student ID").grid(row=0)
    tk.Label(window, text="Name").grid(row=1)
    tk.Label(window, text="Email").grid(row=2)

    entry_id = tk.Entry(window)
    entry_name = tk.Entry(window)
    entry_email = tk.Entry(window)

    entry_id.grid(row=0, column=1)
    entry_name.grid(row=1, column=1)
    entry_email.grid(row=2, column=1)

    tk.Button(window, text='Register', command=register).grid(row=3, column=1, sticky=tk.W, pady=4)
    tk.Button(window, text='Clear', command=clear_fields).grid(row=3, column=2, sticky=tk.W, pady=4)
    window.mainloop()

if __name__ == "__main__":
    register_student_ui()