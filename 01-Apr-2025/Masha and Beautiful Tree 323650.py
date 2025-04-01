# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

def Int(): return int(input())
def arr(): return list(map(int, input().split()))

def solve():
    n = Int()
    a = arr()
    
    opr = 0
    
    def divide_and_conquer(l, r):
        nonlocal opr
        if l == r:
            return [a[l]]
        
        
        
        mid = (l + r) // 2
        left = divide_and_conquer(l, mid)
        right = divide_and_conquer(mid + 1, r)
        
        if left is None or right is None:
            return None
        
        if left[-1] > right[0]:
            left, right = right, left
            opr += 1
        
        merged = left + right
        if merged != sorted(merged):
            return None
        return merged
    
    result = divide_and_conquer(0, n - 1)
    if result is not None:
        return opr
    else:
        return -1

t = Int()
for _ in range(t):
    print(solve())