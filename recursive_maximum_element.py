import random

def max(arr,currentMax):
    if (len(arr)==0):
        print(currentMax)
    else:
        if arr[0] > currentMax:
            currentMax = arr[0]
        max(arr[1:len(arr)],currentMax)


arr = []

for i in range(1,6):
    arr.append(random.randint(6000,12000))

print(arr)
max(arr,0)