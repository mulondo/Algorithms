numbers = [7,5,2,1,3]

def sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1],arr[j]

sort(numbers)

print(numbers)