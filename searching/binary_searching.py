def binary_searhing(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        
        mid = low + (high - low) // 2
        
        # cek jika x berada di tengah
        if arr[mid] == x:
            return mid
        
        # jika x lebih besar, abaikan bagian kiri
        elif arr[mid] < x:
            low = mid + 1
        
        # jika x lebih kecil, abaikan bagian kanan
        else:
            high = mid - 1
        
    # jika sudah, maka elemen
    # tidak hadir
    return -1

if __name__ == '__main__':
    arr = [60, 70, 72, 85, 88, 90, 95]
    x = 90
    
    result = binary_searhing(arr, x)
    if result != -1:
        print("Elemen berada di index", result)
    else:
        print("Elemen tidak berada dalam Array")