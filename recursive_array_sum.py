import random

def sum(arr):
    if (len(arr)==0):
        return 0
    else:
        return arr[0] + sum(arr[1:len(arr)])


arr = []

for i in range(1,101):
    arr.append(random.randint(1,180))

print(arr)
print(sum(arr))
