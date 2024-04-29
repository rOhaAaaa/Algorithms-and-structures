def merge(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def hours_needed(piles, K):
    return sum((pile - 1) // K + 1 for pile in piles)

def min_eating_speed(piles, H):
    sorted_piles = merge_sort(piles)  
    low, high = 1, sorted_piles[-1]

    while low < high:
        K = (low + high) // 2
        if hours_needed(sorted_piles, K) <= H:
            high = K
        else:
            low = K + 1

    return low

piles1 = [3,6,7,11]
H1 = 8
result = min_eating_speed(piles1, H1)
print(min_eating_speed(piles1, H1))

piles2 = [30,11,23,4,20]
H2 = 5
result = min_eating_speed(piles2, H2)
print(min_eating_speed(piles2, H2))

piles3 = [30,11,23,4,20]
H3 = 6
result = min_eating_speed(piles3, H3)
print(min_eating_speed(piles3, H3))

min_eating_speed(piles1, H1), min_eating_speed(piles2, H2), min_eating_speed(piles3, H3)
