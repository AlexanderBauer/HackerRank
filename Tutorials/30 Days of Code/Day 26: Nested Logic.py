# Enter your code here. Read input from STDIN. Print output to STDOUT

def fine():
    # split input into list, structure: [D, M, Y]
    actual      =   input().split()
    expected    =   input().split()

    # calculate differences for D, M, Y
    day_diff    =   int(actual[0]) - int(expected[0])
    month_diff  =   int(actual[1]) - int(expected[1])
    year_diff   =   int(actual[2]) - int(expected[2])

    # calculate fines
    if(day_diff <= 0 and month_diff <= 0 and year_diff <= 0 or year_diff < 0):
        return 0
    elif(day_diff >= 0 and month_diff == 0 and year_diff == 0):
        return 15 * day_diff
    elif(month_diff >= 0 and year_diff == 0):
        return 500 * month_diff
    elif year_diff > 0:
        return 10000

print(fine())