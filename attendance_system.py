import sqlite3

def save_student_to_database(student):
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO student (student_is, name, email) VALUES (?, ?, ?)'),
    (student['student_id'], student['name'], student['email'])
    conn.commit()
    conn.close()

def save_attendance_to_database(attendance_record):
        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)'),
        (attendance_record['student_id'], attendance_record['date'], attendance_record['status'])
        conn.commit()
        conn.close()

def is_unique_student_id(student_id, existing_ids):
      return student_id not in existing_ids
      conn = sqlite3.connect('attendance.db')
      cursor = conn.cursor()
      cursor.execute('SELECT * FROM student WHERE student_id = ?', (student_id,))
      result = cursor.fetchone()
      conn.close()
      return result is None

def fetch_attendance_from_database(student_id):
      conn = sqlite3.connect('attendance.db')
      cursor = conn.cursor()
      cursor.execute('SELECT * FROM Attendance WWHERE student_id = ?', (student_id))
      record = cursor.fetchall()
      conn.close()
      return record