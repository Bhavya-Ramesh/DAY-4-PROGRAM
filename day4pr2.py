def count_non_teaching_staff(staff_users):
    
    return staff_users // 3

def main():
    
    student_users = int(input("Enter the number of student users: "))
    total_users = int(input("Enter the total number of users: "))
    staff_users = int(input("Enter the number of staff users: "))

    
    non_teaching_staff = count_non_teaching_staff(staff_users)

    
    print("\nUser Details:")
    print(f"Student Users: {student_users}")
    print(f"Total Users: {total_users}")
    print(f"Staff Users: {staff_users}")
    print(f"Non-teaching Staff Users (assigned by default): {non_teaching_staff}")

if __name__ == "__main__":
    main()
