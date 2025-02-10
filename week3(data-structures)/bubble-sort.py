def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp=arr[j]
                arr[j]= arr[j+1]
                arr[j+1]= temp
                #can also be written as 'arr[j], arr[j+1] = arr[j+1], arr[j]'
    
    return arr
def main():
    arr = [640, 134, 25, 12, 22, 111, 90]
    
    print("Original array:")
    print(arr)
    sorted_arr = bubble_sort(arr)
    print("Sorted array:")
    print(sorted_arr)
main()