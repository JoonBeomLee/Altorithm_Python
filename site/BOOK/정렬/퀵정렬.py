array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    # 원소가 1개인 경우 종료
    if start >= end: return

    # pivot은 첫 번째 원소
    pivot = start 
    left = start + 1 
    right = end
    
    # 인덱스 교차할때 까지
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때 까지 반복
        while left <= end and array[left] <= array[pivot]: left += 1

        
        # 피벗보다 작은 데이터를 찾을 때 까지 반복
        while right > start and array[right] >= array[pivot]: right -= 1

        # 엇갈렸다면
        # pivot <--> right
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면
        # pivot <--> left
        else:
            array[left], array[pivot] = array[pivot], array[left]

        # 분할 이후 
        # 두 배열 각각 수행
    
    quick_sort(array, start, right - 1)
    quick_sort(array,right + 1, end)

def quick_sort_version_python(array):
    if len(array) <= 1: return array

    pivot = array[0]    # pivot 은 첫 번째 원소
    tail = array[:1]    # pivot 을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼족 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    return quick_sort_version_python(left_side) + [pivot] + quick_sort(right_side)

# quick sort start
quick_sort(array, 0, len(array) - 1)
print(array)

# python version quick sort
print(quick_sort_version_python(array))

