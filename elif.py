a =int(input())
if a%3 == 0 and a%5 == 0:
    print('FizzBizz')
elif a%3 == 0:
    print("Fizz")
elif a%5 == 0:
    print("Bizz")
else:
    print(a)