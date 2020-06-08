if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # sort list by grade, get second lowest grade, 
    students.sort(key = lambda x: x[1])
    lowest_grade      = students[0][1]
    for x, y in students:
        if(y > lowest_grade):
            second_lowest_grade = y
            break

    #sort list by name and print all names with second lowest grade
    students.sort()
    for x, y in students:
        if(y == second_lowest_grade):
            print(x)