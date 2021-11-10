def createArray(n):
    array = []
    for i in range(n):
        percentage = float(input(f"Enter percentage of student {i+1}: "))
        array.append(percentage)
    return array

def sort(array, low, high):
    if high>low:
        mid = (low+high)//2
        sort(array, low, mid)
        sort(array, mid+1, high)
        merged = merge(array, low, high, mid)
        return merged

def merge(array, low, high, mid):
    merge1 = []
    merge2 = []
    n = mid-low+1
    m = high-mid
    for i in range(n):
        merge1.append(array[low+i])
    for i in range(m):
        merge2.append(array[mid+1+i])
    i=0
    j=0
    k=low
    while i<n and j<m:
        if merge1[i]<merge2[j]:
            array[k]=merge1[i]
            i+=1
            k+=1
        else:
            array[k]=merge2[j]
            j+=1
            k+=1
    while i<n:
        array[k] = merge1[i]
        i+=1
        k+=1
    while j<m:
        array[k]=merge2[j]
        j+=1
        k+=1
    return array



n = int(input("Enter total number of students value: "))
array = createArray(n)
low = 0
high = len(array)-1
print(sort(array, low, high))
