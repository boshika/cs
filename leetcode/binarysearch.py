def binary_search(lst, find):
    middle = len(lst) // 2
    print(lst[middle])

    left = lst[:middle]
    right = lst[middle + 1:]

    def logic(left, right, middle_val, index):
        if find == middle_val:
            return middle_val, index
        elif find > middle_val:
            new_middle = len(right) // 2
            l = right[:new_middle]
            r = right[new_middle + 1:]
            return logic(l, r, right[new_middle], new_middle)
        elif find < middle_val:
            new_middle = len(left) // 2
            l = left[:new_middle]
            r = left[new_middle + 1:]
            return logic(l, r, left[new_middle], new_middle)

    return logic(left, right, lst[middle], middle)


print(binary_search([10, 20, 30, 50, 60, 70], 20))
