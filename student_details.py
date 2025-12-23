def student_details(sid, sname, age):
    result = (
        f"Student ID: {sid}\n"
        f"Student Name: {sname}\n"
        f"Age: {age}\n"
    )
    return result


if __name__ == "__main__":
    sid = "001"
    sname = "Priya"
    age = "20"
    print(student_details(sid, sname, age))
