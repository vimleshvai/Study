#! /usr/bin/python3

i= 2

if i%2==0:
    if i in range(2,6):
        print("not weird")
    elif i in range(6,21):
        print("weird")
    elif i > 20:
        print("not weird")
else:
    print("weird")
