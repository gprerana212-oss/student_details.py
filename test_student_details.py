from student_details import student_details


def test_student_details():
    sid = "001"
    sname = "priya"
    age = "20"

    expected_output = (
        "Student ID: 001\n"
        "Student Name: priya\n"
        "Age: 20\n"
    )

    assert student_details(sid, sname, age) == expected_output
