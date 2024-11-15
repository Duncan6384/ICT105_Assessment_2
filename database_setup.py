import sqlite3

# Database setup
def setup_database():
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student (
                   student_id TEXT PRIMARY KEY,
                   name TEXT NOT NULL,
                   email TEXT NOT NULL
                   )
             ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Attendance (
            attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT,
            date TEXT,
            status TEXT,
            FOREIGN KEY (student_id) REFERENCES Student (student_id)
               )
            ''')
    conn.commit()
    conn.close()

# Function to save student to database
def save_student_to_database(student):
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Student (student_id, name, email) VALUES (?, ?, ?)",
                   (student['student_id'], student['name'], student['email']))
    conn.commit()
    conn.close()

# Function to save attendance record to database
def save_attendance_to_database(attendance_record):
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Attendance (student_id, date, status) VALUES (?, ?, ?)",
                   (attendance_record['student_id'], attendance_record['date'], attendance_record['status']))
    conn.commit()
    conn.close()

# Function to check if student id is unique
def is_unique_student_id(student_id):
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Student WHERE student_id = ?", (student_id,))
    result = cursor.fetchone()
    conn.close()
    return result is None

# Function to fetch attendance records
def fetch_attendance_from_database(student_id):
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Attendance WHERE student_id = ?", (student_id,))
    records = cursor.fetchall()
    conn.close()
    return records

# Main function to run the application
if __name__ == "__main__":
    setup_database()