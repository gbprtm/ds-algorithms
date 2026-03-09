def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    
    # membuat array kosong
    L = [0] * n1
    R = [0] * n2
    
    # copy data di array kosong L[] dan R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
        
    i = 0
    j = 0
    k = left
    
    # pindah kan dalam array kosong kembali
    # di arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j+=1
        k += 1
        
    # copy elemen dari L[], jika terdapat beberapa
    while i <  n1:
        arr[k] = L[i]
        i += 1
        k +=1
    
    # copy elemen dari R[], jika terdapat beberapa
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
        
if __name__ == "__main__":
    arr = [8, 3, 2, 9, 7, 1, 5, 4]
   
    merge_sort(arr, 0, len(arr) - 1)
    for i in arr:
        print(i, end=" ")
    print()
    