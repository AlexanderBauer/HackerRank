if __name__ == '__main__':
    marks = {}
    # loop through all students and add marks to dict
    for _ in range(int(input())):
        name, *line = input().split()
        scores      = list(map(float, line))
        marks[name] = scores
    # read query, calculate average and print result
    query   = input()
    average = format(sum(marks[query]) / len(marks[query]), '.2f')
    print(average)