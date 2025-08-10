# Step 1: Create a list of student details
students = [
    ["Grade 10", 15, "Math", "Rice", 101],
    ["Grade 9", 14, "English", "Beans", 102],
    ["Grade 11", 16, "Biology", "Yam", 103],
    ["Grade 10", 15, "Chemistry", "Pasta", 104],
    ["Grade 12", 17, "Physics", "Plantain", 105]
]

# Step 2: Convert the list into a dictionary
# The roll number is used as the key, and the rest of the details as the value
student_dict = {}
for student in students:
    roll_no = student[4]
    details = {
        "grade": student[0],
        "age": student[1],
        "fav_subject": student[2],
        "fav_food": student[3]
    }
    student_dict[roll_no] = details

# Step 3: Display the dictionary
print("Student Dictionary:\n")
for roll, info in student_dict.items():
    print(f"Roll No {roll}: {info}")
