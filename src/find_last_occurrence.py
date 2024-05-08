def find_last_occurrence(haystack, needle):
    n = len(haystack)
    m = len(needle)
    last_index = -1
    comparisons = 0
    if m == 0:
        return -1, 0
    for i in range(n - m + 1):
        for j in range(m):
            comparisons += 1
            if haystack[i + j] != needle[j]:
                break
        else:
            last_index = i + m - 1
    return last_index, comparisons

haystack = "hello world, hello sea, hello sky"
needle = "hello"
result = find_last_occurrence(haystack, needle)
print(f"Кінцевий індекс: {result[0]}, Кількість порівнянь: {result[1]}")
