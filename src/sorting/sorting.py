# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):

    sorted = []
    ai = 0
    bi = 0
    count = len(arrA) + len(arrB)

    while len(sorted) < count:
        if ai >= len(arrA):
            sorted.append(arrB[bi])
            bi += 1
        elif bi >= len(arrB):
            sorted.append(arrA[ai])
            ai += 1
        elif arrA[ai] < arrB[bi]:
            sorted.append(arrA[ai])
            ai += 1
        elif arrA[ai] > arrB[bi]:
            sorted.append(arrB[bi])
            bi += 1

    return sorted

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here

    if len(arr) == 0:
        return None

    if len(arr) == 1:
        return arr  # base case recursion

    else:

        middle = (len(arr)) // 2
        #print(middle, 'middle')
        # print(arr[middle])

        lhs = arr[:middle]
        rhs = arr[middle:]
        # print(lhs)
        # print(rhs)

    return merge(merge_sort(lhs), merge_sort(rhs))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass


arr = [3, 1, 5, 2, 7]
print(arr)
print(merge_sort(arr))
