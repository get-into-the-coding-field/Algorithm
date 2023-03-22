import time

insert_start = time.time()
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j+1] = key
    return arr

insertion_sort([5,10,2,3,8,4,5,10,2,3,8,4,5,10,2,3,8,4,5,10,2,3,8,4,5,10,2,3,8,4]*1000)
insert_end = time.time()
print(f"삽입 정렬 시간:  {insert_end - insert_start:.5f} sec")

select_start = time.time()
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # i번째 원소부터 끝까지 중 가장 작은 원소를 찾는다
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # i번째 원소와 가장 작은 원소를 교환한다
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

selection_sort([5,10,2,3,8,4,5,10,2,3,8,4,5,10,2,3,8,4,5,10,2,3,8,4,5,10,2,3,8,4]*1000)
select_end = time.time()
print(f"선택 정렬 시간:  {select_end - select_start:.5f} sec")

bubble_start = time.time()
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

bubble_sort([5,10,2,3,8,4,5,10,2,3,8,4,5,10,2,3,8,4,5,10,2,3,8,4,5,10,2,3,8,4]*1000)
bubble_end = time.time()
print(f"버블 정렬 시간:  {bubble_end - bubble_start:.5f} sec")


quick_start = time.time()
def quick_sort(arr):
    
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]
    left, equal, right = [], [], []
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            right.append(num)
        
    return quick_sort(left) + equal + quick_sort(right)
quick_end = time.time()
quick_sort([5,10,2,3,8,4,5,10,2,3,8,4,5,10,2,3,8,4,5,10,2,3,8,4,5,10,2,3,8,4]*1000)
print(f"퀵 정렬 시간:  {quick_end - quick_start:.5f} sec")


merge_start = time.time()
def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    merged += left[left_index:]
    merged += right[right_index:]
    
    return merged
merge_end = time.time()
print(merge_sort([5,10,2,3,8,4,5,10,2,3,8,4,5,10,2,3,8,4,5,10,2,3,8,4,5,10,2,3,8,4]*1000))
print(f"병합 정렬 시간:  {merge_end - merge_start:.5f} sec")