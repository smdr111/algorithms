from random import randrange

def quick_sort(arr, left=0, right=None):
    # First call: no bounds given, so sort the whole list
    if right is None:
        right = len(arr) - 1

    # Keep going while the current section has 2+ elements
    while left < right:

        # 1. Pick a random pivot and move it to the front of the section
        p = randrange(left, right + 1)
        arr[left], arr[p] = arr[p], arr[left]

        # 2. 3-way partition around the pivot value
        pivot = arr[left]
        lt, i, gt = left, left + 1, right

        while i <= gt:
            if arr[i] < pivot:
                # smaller than pivot: send it to the "less" zone
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                # bigger than pivot: send it to the "greater" zone
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1          # don't move i: the swapped-in value is unchecked
            else:
                # equal to pivot: leave it in the middle zone
                i += 1

        # 3. Recurse on the smaller side, loop on the larger side
        if lt - left < right - gt:
            quick_sort(arr, left, lt - 1)    # sort the "less" zone
            left = gt + 1                    # then loop on the "greater" zone
        else:
            quick_sort(arr, gt + 1, right)   # sort the "greater" zone
            right = lt - 1                   # then loop on the "less" zone

    return arr
