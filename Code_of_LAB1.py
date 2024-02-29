def set_pivot(elem, left, right):
    pivot = elem[right]
    i = left - 1
    for j in range(left, right):
        if elem[j] <= pivot:  
            i += 1
            elem[i], elem[j] = elem[j], elem[i]
    elem[i+1], elem[right] = elem[right], elem[i+1]
    return i + 1

def quick_select(elem, left, right, k):
    if left <= right:
        pivot_idx = set_pivot(elem, left, right)
        if right - pivot_idx == k - 1:  
            return elem[pivot_idx]
        elif right - pivot_idx > k - 1:  
            return quick_select(elem, pivot_idx + 1, right, k)
        else:  
            return quick_select(elem, left, pivot_idx - 1, k - (right - pivot_idx + 1))

def find_kth_largest(nums, k):
    return quick_select(nums, 0, len(nums) - 1, k)

# Тестування функції
nums = [3, 7, 22, 9, 25, 2, 11, 18]
k = 3
kth_largest = find_kth_largest(nums, k)
print(f"{k}-й найбільший елемент: {kth_largest}")
print(f"Позиція {k}-го найбільшого елемента в масиві: {nums.index(kth_largest)}")
