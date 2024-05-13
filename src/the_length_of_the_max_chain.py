def can_transform(w1, w2):
    if len(w1) != len(w2) + 1:
        return False
    for i in range(len(w1)):
        if w1[:i] + w1[i+1:] == w2:
            return True
    return False

def max_chain_length(words):
    words.sort(key=len)
    max_len = {}
    max_chain = 1
    
    for word in words:
        max_len[word] = 1 
        for prev_word in [w for w in words if len(w) == len(word) - 1]:
            if can_transform(word, prev_word):
                max_len[word] = max(max_len[word], max_len[prev_word] + 1)
        max_chain = max(max_chain, max_len[word])
    
    return max_chain

def solve(file_path, output_file_path):
    with open(file_path, 'r') as file:
        n = int(file.readline().strip())
        words = [file.readline().strip() for _ in range(n)]

    result = max_chain_length(words)

    with open(output_file_path, 'w') as file:
        file.write(str(result))

file_path = r'tests\resources\wchain.in.txt'
output_file_path = r'tests\resources\wchain.out.txt'

solve(file_path, output_file_path)
