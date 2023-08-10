def swap_elems(in_list: list, i, j):
    tmp = in_list[i]
    in_list[i] = in_list[j]
    in_list[j] = tmp

def quicksort(in_list: list, low: int, high: int) -> list:
    pivot_index = high - 1
    pivot = in_list[pivot_index]
    i = low - 1
    j = low

    print(in_list)

    if low >= pivot_index:
        return None

    while j < pivot_index:
        if in_list[j] < pivot:
            i = i + 1
            swap_elems(in_list, i, j)
        j = j + 1

    swap_elems(in_list, pivot_index, i + 1)

    quicksort(in_list, low, i + 1)
    quicksort(in_list, i + 2, high)

    return in_list

if __name__ == "__main__":
    # list_of_ints : list[int] = [10, 80, 30, 90, 40]
    # After 1 stage of sorting, [10, 30, 40, 90, 80]
    # Here 40 is the pivot
    list_of_ints: list[int] = [23, 12, 3, 6, 8, 9]
    print("Before sorting, list =", list_of_ints)
    print("After sorting, list =", quicksort(list_of_ints, 0, len(list_of_ints)))
