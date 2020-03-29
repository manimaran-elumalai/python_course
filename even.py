import random

rand = random.randint(999,999999)

print("Number generated")
print(rand)

if(rand%2 == 0):
    print("Even!")
else:
    print("Odd!")