def merge(list1: list[int], list2: list[int]) -> list[int]:
    combined = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    combined.extend(list1[i:])
    combined.extend(list2[j:])
    return combined


def merge_sort(my_list: list[int]) -> list[int]:
    if len(my_list) < 2:
        return my_list

    mid = len(my_list) // 2
    left = merge_sort(my_list[:mid])
    right = merge_sort(my_list[mid:])
    return merge(left, right)
