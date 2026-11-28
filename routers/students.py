import csv
from pathlib import Path
from fastapi import APIRouter, HTTPException

router = APIRouter()

CSV_FILE = Path(__file__).resolve().parent.parent / "clean.csv"


def load_students():
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        students = []

        for row in reader:
            row["id"] = int(row["id"])
            students.append(row)

    return students


@router.get("/students")
def get_students(dept: str = "CSE"):
    students = load_students()

    result = [
        student for student in students
        if student["dept"].lower() == dept.lower()
    ]

    return {
        "department": dept,
        "students": result
    }


@router.get("/students/{student_id}")
def get_student(student_id: int):
    students = load_students()

    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )