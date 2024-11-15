import unittest
from attendance_system import is_unique_student_id, save_attendance_to_database
import attendance_system

class  TestAttendanceSystem(unittest.TestCase):
    def test_is_unique_student_id(self):
        self.assertTrue(is_unique_student_id("test_id"))
        self.assertTrue(attendance_system("test_id"))
        self.assertTrue(save_attendance_to_database("test_id"))
        
if __name__ == '__main__':
    unittest.main()