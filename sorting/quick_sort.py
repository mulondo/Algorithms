def quick_sort(elements):
    length = len(elements)
    if length<=1:
        return elements
    else:
        pivot = elements.pop()
        item_lower = []
        item_greater = []

        for item in elements:
            if item > pivot:
                item_greater.append(item)

            else:
                item_lower.append(item)
    return quick_sort(item_lower) + [pivot] + quick_sort(item_greater)


numbers = [8,3,9,7,2,4,0,10]
print(quick_sort(numbers))