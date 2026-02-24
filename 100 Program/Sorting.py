# Sort a list without using sort() method

def sort_list(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                # Swap
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

numbers = list(map(int, input().split()))

sorted_numbers = sort_list(numbers)

print(*sorted_numbers)


#Output:
#Enter numbers: 34 67 23 89 12
#12 23 34 67 89
#Enter numbers: 5 6 5 7 8 6
#5 5 6 6 7 8
