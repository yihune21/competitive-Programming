# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

def Int(): return int(input())
def arr(): return list(map(int, input().split()))

def solve():
    n = Int()
    stones_costs = arr()
    m = Int()
   
    prefix_original = [0] * (n + 1)
    
    for i in range(1, n + 1):
        prefix_original[i] = prefix_original[i - 1] + stones_costs[i - 1]
    
    sorted_v = sorted(stones_costs)
    prefix_sorted = [0] * (n + 1)
    
    for i in range(1, n + 1):
        prefix_sorted[i] = prefix_sorted[i - 1] + sorted_v[i - 1]
    
    output = []
    
    for _ in range(m):
        type_q, l, r = arr()
        
        if type_q == 1:
            res = prefix_original[r] - prefix_original[l - 1]
        else:
            res = prefix_sorted[r] - prefix_sorted[l - 1]
            
        output.append(res)
    
    print('\n'.join(map(str, output)))
    return 


t = 1
# t = Int()

for _ in range(t):
    solve()

