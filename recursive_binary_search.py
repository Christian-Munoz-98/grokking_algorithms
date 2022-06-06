'''
def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low+high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid +1
    return None

my_list = [1,3,5,7,9]

print(binary_search(my_list,3))
print(binary_search(my_list,-1))
'''

def binary_search(list,item,low,high):
    if low>high:
        print("Not found")
    else:
        mid = (low+high)//2
        guess = list[mid]
        if guess == item:
            print(f"Founded in index {mid}")
        elif guess > item:
            binary_search(list,item,low,mid-1)
        else:
            binary_search(list,item,mid+1,high)


my_list = [1,3,5,7,9,11,13,15,17]

binary_search(my_list,11,0,len(my_list)-1)
binary_search(my_list,-1,0,len(my_list)-1)
    