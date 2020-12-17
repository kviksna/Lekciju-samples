
try:
    print(5/0)
except ZeroDivisionError: print("Error: ZeroDivisionError")

res = 1
print(id(res)) #adrese RAM'ā


w=5
s=10
print('w: {}'.format(w))
#salary = 'Salary: {}'.format(salary)
#salary2 = 'Salary: {}{}'.format(salary, 2)

# f'Salary: {}'.format(salary)

# typeof: sub instance
a=5
b=4
if a > b and True or True:
    print("a > b")
elif a==b:
    print("a==b")
else : print("else")

# https://www.programiz.com/python-programming/examples/odd-even
if 5 % 2 > 0:
    print("Odd")
else:
    print("Even")


# https://www.programiz.com/python-programming/examples/leap-year

# Python program to check if year is a leap year or not

year = 2000

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))

# print("{}{}{}={}".format(a,b,c))
# print(f"{a}{b}{c}={x}")
