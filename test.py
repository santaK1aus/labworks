import re
regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
email='hi@gmail.com'
if re.search(regex,email):
    print('hi')
else:
    print('damn')
