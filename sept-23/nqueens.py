def is_diagonal(permutation):
    
    n = len(permutation)
    
    for i in range(n):
        for j in range(i+1, n):
            if abs(i - j) == abs(permutation[i] - permutation[j]):
                return True
    return False

# modify this to test in-line to check first

def permutations(n):
    
    nums = [i for i in range(n)]
    used = [False] * n
    def backtrack(path, index, used):
        
        if index == n:
            results.append(path[:])
            return
        
        for i in range(n):
            if not used[i]:
                used[i] = True
                path.append(i)
                if not is_diagonal(path):
                    backtrack(path, index + 1, used)
                path.pop()
                used[i] = False
            
    results = []
    backtrack([], 0, used)

    return len(results)


print(permutations(13))