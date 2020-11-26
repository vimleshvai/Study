val = input("Enter number :")

var1=int(val)

for i in range(var1):
     if i % 15 == 0:
             print("fizzbuzz")
             continue
     elif i % 3 == 0:
             print("fizz")
             continue
     elif i % 5 == 0:
             print("buzz")
             continue
     print(i)
