import pandas as pd

data={
    "Name":["Parth","Antra","Arjun","Nikhil","Sohum","Uma"],
    "Marks":[77,98,84,89,95,57]
}

student=pd.DataFrame(data)

print(student)
print(student[student["Marks"]>90])
print(student["Marks"].mean())
print(student["Marks"].max())
print(student["Marks"].min())
print(student.sort_values("Marks",ascending=False))
