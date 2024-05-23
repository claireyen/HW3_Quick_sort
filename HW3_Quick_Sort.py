def quick_sort(array, tab=0):
    if len(array) <= 1:
        return array
    pivot = array[0]
    left = [x for x in array[1:] if x <= pivot]
    right = [x for x in array[1:] if x > pivot]
    
    # 印出過程
    print('  ' * tab + 'Pivot: ' + str(pivot))
    print('  ' * tab + 'Left: ' + str(left))
    print('  ' * tab + 'Right: ' + str(right))

    return quick_sort(left, tab+1) + [pivot] + quick_sort(right, tab+1)



data = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]

print('Original:' + str(data) + '\n')

sorted_data = quick_sort(data)

print('\nSorted:' + str(sorted_data))
