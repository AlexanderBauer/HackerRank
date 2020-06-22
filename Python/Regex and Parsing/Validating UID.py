import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        # contain at least 2 uppercase letters
        assert re.search(r'[A-Z]{2}', u)
        # contain at least 3 digits
        assert re.search(r'\d{3}', u)
        # contain only alphanumeric characters
        assert not re.search(r'[^\w]', u)
        # no character should repeat
        assert not re.search(r'(.)\1', u)
        # contains exactly 10 chars
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')