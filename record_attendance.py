from tkinter import messagebox
from database_setup import save_attendance_to_database


def record_attendance_ui():
    def record():
        student_id = entry_id.get() # type: ignore
        date = entry_date.get() # type: ignore
        status = entry_status.get() # type: ignore
        attendance_record = {"student_id": student_id, "date": date, "status": status}
        save_attendance_to_database(attendance_record)
        messagebox.showinfo("Success", "Attendance recorded successfully!")

window = tk.tk() # type: ignore
window.title("Record Attendance")

tk.Label(window, text="Student ID").grid(row=0) # type: ignore
tk.Label(window, text="date (YYYY-MM-DD)").grid(row=1) # type: ignore
tk.Label(window, text="Status (Present/Absent)").grid(row=2) # type: ignore

entry_id = tk.Entry(window) # type: ignore
entry_date = tk.Entry(window) # type: ignore
entry_status = tk.Entry(window) # type: ignore

entry_id.grid(row=0, colum=1)
entry_date.grid(row=1, colum=1)
entry_status.grid(row=2, colum=1)

tk.Button(window, text='Record', command=record).grid(row=3, colum=1, sticky=tk.W, pady=4) # type: ignore
window.mainloop()