"""Программа получает на вход три натуральных числа A, B и C через пробел.

Вам необходимо вывести "YES" в том случае, если A + B = C и вывести NO в противном случае."""

a,b,c = map(int, input().split())
if a+b == c:
    print("YES")
else:
    print('NO')