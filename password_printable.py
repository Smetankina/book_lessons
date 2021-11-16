#password
from string import printable

for i in printable:
    for j in printable:
        print(i, j, end ='')
    print()