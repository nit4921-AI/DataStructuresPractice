
import math



def gradingStudents(grades):
    results=[]
    for i in grades:
        if i >= 38 and ((math.ceil(i/5))*5)-i<3:
            results.append((math.ceil(i/5))*5)
        elif i >= 38 and ((math.ceil(i/5))*5)-i<3:
            results.append(i)
        else:
            results.append(i)
    return results
if __name__ == "__main__":
    n = int(input("Enter number of grades: "))
    grades = []
    
    for _ in range(n):
        grades.append(int(input("Enter grade: ")))
    
    result = gradingStudents(grades)
    
    print("\nFinal Grades:")
    for r in result:
        print(r)