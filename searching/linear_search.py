def search(arr, x):
    n = len(arr)
    
    # cari x
    for i in range(0, x):
        if (arr[i] == x):
            return i
    return -1
    
if __name__ == "__main__":
    arr = [72, 85, 60, 90, 75, 88, 70, 95]
    x = 90
    
    result = search(arr, x)
    if (result == -1):
        print("Elemen tidak ada dalam Array")
    else:
        print("Elemen berada dalam index", result)
        