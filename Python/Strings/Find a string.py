def count_substring(string, sub_string):
    counter = 0
    for i in range(len(string) + 1):
        if string.startswith(sub_string, i):
            counter += 1
    return counter