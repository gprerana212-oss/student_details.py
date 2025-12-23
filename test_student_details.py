from student_details import student_details

def test_student_details():
    result = student_details("001", "priya", 20)
    expected = (
        "studentid:001\n"
        "studentname:priya\n"
        "studentage:20"
    )
    assert result == expected

