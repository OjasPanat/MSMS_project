# --- Main Application Loop ---
def main():
    """Main function to run the MSMS application."""
    load_data() # Load all data from file at startup.

    while True:
        print("\n===== MSMS v2 (Persistent) =====")
        print("1. Check-in Student")
        print("2. Print Student Card")
        print("3. Update Teacher Info")
        print("4. Remove Student")
        print("q. Quit and Save")
        
        choice = input("Enter your choice: ")
        
        made_change = False # A flag to track if we need to save
        if choice == '1':
            try:
                student_id = int(input("Enter student ID: "))
                course_id = input("Enter course name: ")
                check_in(student_id, course_id)
                made_change = True
            except ValueError:
                print("ID is invalid. Please enter a number.")
            # TODO: Get student_id and course_id from user, then call check_in().
        elif choice == '2':
            try:
                student_id = int(input("Enter student ID: "))
                print_student_card(student_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
            pass # No change made, so no save needed
        elif choice == '3':
            try:
                teacher_id = int(input("Enter teacher ID to update: "))
                name = input("Enter new name (leave blank to skip): ")
                speciality = input("Enter new speciality (leave blank to skip): ")
                update_fields = {}
                if name.strip():
                    update_fields["name"] = name
                if speciality.strip():
                    update_fields["speciality"] = speciality
                if update_fields:
                    update_teacher(teacher_id, **update_fields)
                    made_change = True
                else:
                    print("No updates provided.")
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == '4':
            try:
                student_id = int(input("Enter student ID to remove: "))
                remove_student(student_id)
                made_change = True
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice.lower() == 'q':
            print("Saving final changes and exiting.")
            break
        else:
            print("Invalid choice.")
            
        if made_change:
            save_data() # Save the data immediately after any change.

    save_data() # One final save on exit.

# --- Program Start ---
if __name__ == "__main__":
    main()