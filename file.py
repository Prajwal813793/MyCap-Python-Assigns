import csv

def write_csv(records):
   
    with open("students.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "age", "grade", "address"])
        writer.writeheader()
        writer.writerows(records)

def read_csv():
    
    try:
        with open("students.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []

def add_record():
   
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    address = input("Enter student address: ")
    records.append({"name": name, "age": age, "grade": grade, "address": address})
    print("Student record added successfully!")

def modify_record():
    
    name = input("Enter student name: ")
    for record in records:
        if record["name"] == name:
            record["age"] = input("Enter new age: ")
            record["grade"] = input("Enter new grade: ")
            record["address"] = input("Enter new address: ")
            print("Student record modified successfully!")
            return
    print("Student not found.")

def delete_record():
   
    name = input("Enter student name: ")
    for record in records:
        if record["name"] == name:
            records.remove(record)
            print("Student record deleted successfully!")
            return
    print("Student not found.")


records = read_csv()

while True:
    print("1. Add student record")
    print("2. Modify student record")
    print("3. Delete student record")
    print("4. View all student records")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_record()
    elif choice == "2":
        modify_record()
    elif choice == "3":
        delete_record()
    elif choice == "4":
        for record in records:
            print(record)
    elif choice == "5":
        write_csv(records)
        break
    else:
        print("Invalid choice.")
