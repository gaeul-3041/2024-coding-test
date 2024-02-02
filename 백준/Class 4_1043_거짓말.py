n, m = map(int, input().split())
truth = set(list(map(int, input().split()))[1:])
answer = 0

party = []
for _ in range(m):
    party.append(list(map(int, input().split()))[1:])
    
## Not Finished