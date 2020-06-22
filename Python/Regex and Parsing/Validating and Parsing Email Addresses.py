import email.utils
import re

def validate_email(email):
    try:
        assert re.search(r'^[A-Za-z][A-Za-z0-9-_.]+@[A-Za-z]+[.][A-Za-z]{1,3}$', email)
    except:
        return False
    else:
        return True

if __name__ == '__main__':
    for _ in range(int(input())):
        line    =   input()
        tpl     =   email.utils.parseaddr(line)
        if(validate_email(tpl[1])):
            print(line)