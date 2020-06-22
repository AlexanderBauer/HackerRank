import re

def validate_cc(number):
    try:
        # check basic structure
        assert re.search(r'^[456][\d]{3}[-]?[\d]{4}[-]?[\d]{4}[-]?[\d]{4}$', number)
        # check repetitions
        number  =   number.replace('-', '')
        reps    =   1
        for x in range(1, len(number)):
            if(number[x] == number[x-1]):
                reps += 1
                assert reps < 4
            else:
                reps = 1
    except:
        return 'Invalid'
    else:
        return 'Valid'

if __name__ == '__main__':
    for _ in range(int(input())):
        print(validate_cc(input()))