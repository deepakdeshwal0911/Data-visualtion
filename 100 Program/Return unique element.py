# Return unique elements from a list using function

def unique_elements(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

# Read space-separated numbers
numbers = list(map(int, input().split()))

result = unique_elements(numbers)

print(*result)

#Output:
#Enter numbers: 1 2 3 2 4 1
#1 2 3 4
#Enter numbers: 5 6 5 7 8 6
#5 6 7 8
