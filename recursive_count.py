import random

def count(arr):
    if (len(arr)==0):
        return 0
    else:
        return 1 + count(arr[1:len(arr)])


arr = []

for i in range(1,114):
    arr.append(random.randint(1,180))

print(count(arr))