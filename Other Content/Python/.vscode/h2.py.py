if __name__ == '__main__':
    n = int(input("Enter the number of students (2 <= n <= 10): "))
    
    # Check if n is within the specified range
    if n < 2 or n > 10:
        print("Number of students must be between 2 and 10.")
    else:
        student_marks = {}
        
        # Input student data
        for _ in range(n):
            name, *marks = input("Enter student name and 3 marks (0 <= marks <= 100): ").split()
            marks = list(map(float, marks))
            
            # Check if the number of marks is 3 and if they are within the specified range
            if len(marks) != 3 or any(mark < 0 or mark > 100 for mark in marks):
                print("Marks should be three values between 0 and 100.")
                break
            
            student_marks[name] = marks
        
        else:
            query_name = input("Enter the name of the student to calculate the average: ")
            
            # Check if the query_name exists in the dictionary
            if query_name in student_marks:
                average = sum(student_marks[query_name]) / len(student_marks[query_name])

                print("{:.2f}".format(average))
            else:
                print("Student not found in the records.")
