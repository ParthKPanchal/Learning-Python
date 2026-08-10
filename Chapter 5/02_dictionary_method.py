marks={
    "Antra": 98,
    "Parth":77,
    "Nikhil":84,
}

print(marks.items())
print(marks.keys())
print(marks.values())
print(marks.update({"Parth":49,"Ankita":70}))
print(marks)
print(marks.get("Antra")) # Prints None
print(marks["Antra"]) # return an error