from collections import deque

answer = [-1, 0, 0, 0]  # 시작점, 도넛, 막대, 8자
start = [[] for i in range(1000001)]  # 최대 1,000,000개 노드가 있으므로 길이 1,000,001로 정의
end = [[] for i in range(1000001)]
visited = [0 for i in range(1000001)]

def bfs(p):
    q = deque([p])
    visited[p] = 1
    
    while q:
        n = q.popleft()
        # 다음이 없는 노드는 막대 그래프에서만 등장
        if len(start[n]) == 0:
            answer[2] += 1
            return
        # 8자 그래프는 첫 노드가 반드시 2개의 노드와 양방향 통행이 존재
        if len(start[n]) == 2 and len(end[n]) == 2:
            answer[3] += 1
            return
        # 그 외의 경우 일단 다음 노드를 추적
        for i in start[n]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

    # 만약 q를 모두 소모했다면 한 바퀴를 돌았다는 뜻으로 도넛 그래프에 해당
    answer[1] += 1

def solution(edges):
    # 각 노드의 통행 정보 저장
    for s, e in edges:
        start[s].append(e)
        end[e].append(s)

    # 시작점은 2개 이상의 나가는 길 + 0개의 들어오는 길이 있는 유일한 지점
    for i in range(1000001):
        if len(start[i]) >= 2 and len(end[i]) == 0:
            answer[0] = i
            visited[i] = 1
            break
            
    sp = answer[0]

    # 시작점에서 파생된 노드에 대해 각각 BFS 수행
    for p in start[sp]:
        end[p].remove(sp)
        bfs(p)
            
    return answer
