import math

def heapify(list, count):
    start = math.floor((count-2)/2)

    while start >= 0:
        siftDown(list, start, count - 1)
        start -= 1

def siftDown(list, start, end):
    root = start
    child = (2 * root) + 1
    while child <= end:
        swap = root
        if list[swap] < list[child]:
            swap = child
        if child + 1 <= end and list[swap] < list[child+1]:
            swap = child + 1
        if root == swap:
            return
        list[root], list[swap] = list[swap], list[root]
        root = swap
        child = ( 2 * root ) + 1

def heapSort(arr):
    size = len(arr)
    heapify(arr, size)
    end = size-1
    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]
        end = end - 1
        siftDown(arr, 0, end)

if __name__ == "__main__":
    arr =  [6, 5, 3, 1, 8, 7, 2, 4]
    heapSort(arr)
    print(arr)