def bubble_sort(arr):
    """冒泡排序：相邻元素两两比较，较大者后移，每轮将最大值沉到末尾。"""
    n = len(arr)
    for i in range(n - 1):
        swapped = False  # 优化：若本轮无交换则已有序
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def selection_sort(arr):
    """选择排序：每轮在未排序部分选出最小值，与当前位交换。"""
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("排序前:", data)

    data1 = data.copy()
    bubble_sort(data1)
    print("冒泡排序后:", data1)

    data2 = data.copy()
    selection_sort(data2)
    print("选择排序后:", data2)

    print("hello world")