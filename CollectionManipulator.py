def main_program():
    records = []       
    db = {}            
    all_subjects = set() 

    print("--- STUDENT DATA ORGANIZER ---")
    print("Manage your student records easily.\n")

    while True:
        print("Menu Options:")
        print("1) Add New Student")
        print("2) View All Students")
        print("3) Edit Student Info")
        print("4) Remove Student")
        print("5) List Unique Subjects")
        print("6) Exit")
        
        choice = input("Select an option: ").strip()
        print() 

        if choice == '1':
            print("Enter Details:")
            id_num = int(input("Enter ID: "))
            
            if id_num in db:
                print("Error: This ID already exists!\n")
                continue
                
            name = input("Enter Name: ").strip()
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ").strip()
            dob = input("Enter DOB (YYYY-MM-DD): ").strip()
            
            sub_input = input("Enter Subjects (use commas): ")
            sub_set = {s.strip() for s in sub_input.split(",") if s.strip()}

            # Tuple for fixed data
            fixed_data = (id_num, dob)

            info = {
                "name": name,
                "age": age,
                "grade": grade,
                "subjects": sub_set,
                "fixed": fixed_data
            }

            db[id_num] = info
            records.append(info)
            all_subjects.update(sub_set)

            print("Success: Student record added!\n")

        elif choice == '2':
            if not records:
                print("No records available.\n")
                continue

            print("--- Registered Students ---")
            for item in records:
                s_id = item["fixed"][0]
                s_name = item["name"]
                s_age = item["age"]
                s_grade = item["grade"]
                s_subs = ", ".join(item["subjects"])

                # Primary display using f-string
                print(f"ID: {s_id} | Name: {s_name} | Age: {s_age} | Grade: {s_grade} | Subjects: {s_subs}")
            print("---------------------------\n")

        elif choice == '3':
            search_id = int(input("Enter Student ID to update: "))
            
            if search_id in db:
                print("1. Update Age\n2. Update Subjects")
                edit_choice = input("Choice: ").strip()

                if edit_choice == '1':
                    db[search_id]["age"] = int(input("Enter new Age: "))
                    print("Age updated.\n")
                    
                elif edit_choice == '2':
                    new_subs = input("Enter new subjects (comma-separated): ")
                    updated_set = {s.strip() for s in new_subs.split(",") if s.strip()}
                    
                    db[search_id]["subjects"] = updated_set
                    
                    all_subjects.clear()
                    for s in db.values():
                        all_subjects.update(s["subjects"])
                        
                    print("Subjects updated.\n")
                else:
                    print("Invalid choice.\n")
            else:
                print("Student not found.\n")

        elif choice == '4':
            del_id = int(input("Enter Student ID to remove: "))
            
            if del_id in db:
                for item in records:
                    if item["fixed"][0] == del_id:
                        records.remove(item)
                        break
                
                # del keyword requirement
                del db[del_id]
                
                all_subjects.clear()
                for s in db.values():
                    all_subjects.update(s["subjects"])

                print(f"Record for ID {del_id} deleted.\n")
            else:
                print("ID not found.\n")

        elif choice == '5':
            print("--- Course Subjects ---")
            if all_subjects:
                print(", ".join(all_subjects))
            else:
                print("No subjects found.")
            print("-----------------------\n")

        elif choice == '6':
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main_program()