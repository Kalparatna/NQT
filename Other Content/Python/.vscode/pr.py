if __name__ == '__main__':
    n = int(input("Enter the number of students: "))
    student_marks = {}
    
    # Input data and populate the dictionary
    for _ in range(n):
        name, *line = input("Enter student name and scores: ").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    
    query_name = input("Enter the name of the student to find the average score: ")
    
    if query_name in student_marks:
        # Calculate the average score for the specified student
        average_score = sum(student_marks[query_name]) / len(student_marks[query_name])
        
        # Print the average score with 2 decimal places
        print(f"{query_name}'s average score: {average_score:.2f}")
    else:
        print(f"No data found for {query_name}")
