# BFS / DFS (그래프 탐색)

## 한 줄 요약
**그래프(또는 격자)의 모든 노드를 빠짐없이 방문**하는 두 가지 방식. BFS는 가까운 데부터(너비), DFS는 한 길로 끝까지(깊이).

```
   1
  / \
 2   3
 │   │
 4   5

BFS 방문 순서: 1 → 2 → 3 → 4 → 5  (레벨별)
DFS 방문 순서: 1 → 2 → 4 → 3 → 5  (한 길 끝까지)
```

## BFS — 너비 우선 탐색

**큐(deque)** 사용. 현재 노드의 이웃을 모두 큐에 넣고, 큐 앞에서 꺼내 처리.

```python
from collections import deque

def bfs(start, graph):
    visited = {start}
    q = deque([start])
    while q:
        node = q.popleft()
        # 노드 처리
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
```

### BFS의 핵심 성질 ⭐
**간선 가중치가 모두 같으면, 시작점으로부터의 최단 거리를 보장**.

→ "**최단 거리/최소 횟수**" 문제는 일단 BFS 의심.

```python
def shortest(start, end, graph):
    visited = {start}
    q = deque([(start, 0)])           # (노드, 거리)
    while q:
        node, dist = q.popleft()
        if node == end: return dist
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, dist + 1))
    return -1
```

## DFS — 깊이 우선 탐색

**스택 또는 재귀** 사용. 한 길을 끝까지 따라가다가 막히면 되돌아옴.

### 재귀 버전 (가장 자주 씀)
```python
def dfs(node, graph, visited):
    visited.add(node)
    # 노드 처리
    for nxt in graph[node]:
        if nxt not in visited:
            dfs(nxt, graph, visited)

dfs(start, graph, set())
```

### 명시적 스택 버전
```python
def dfs_iter(start, graph):
    visited = {start}
    stack = [start]
    while stack:
        node = stack.pop()
        # 처리
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                stack.append(nxt)
```

재귀 한도 걱정되면 명시적 스택. 보통 재귀가 더 짧고 직관적.

## 격자에서 BFS / DFS

가장 자주 나오는 패턴.

```python
from collections import deque

def bfs_grid(grid, sx, sy):
    n, m = len(grid), len(grid[0])
    visited = [[False]*m for _ in range(n)]
    q = deque([(sx, sy)])
    visited[sx][sy] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if grid[nx][ny] == 1:    # 갈 수 있는 칸 조건
                    visited[nx][ny] = True
                    q.append((nx, ny))
```

## BFS vs DFS 어느 걸 쓸까

| 상황 | 선택 |
|---|---|
| **최단 거리** (가중치 동일) | **BFS** ⭐ |
| 최단 거리 (가중치 다름) | 다익스트라 |
| 모든 경로 / 깊은 탐색 | DFS |
| 모든 노드 방문만 하면 됨 | 둘 다 OK (취향) |
| 사이클 / 백트래킹 | DFS |
| 메모리 | DFS가 보통 적음 (재귀 깊이만큼) |
| 가장 깊은 / 끝까지 | DFS |
| 레벨별 처리 | BFS |

**한 줄 결론**: "최단"이라는 단어 보이면 BFS, 그 외엔 DFS도 괜찮음.

## 자주 등장하는 응용

### 1. 연결 요소 개수 (섬의 개수)
```python
def count_islands(grid):
    n, m = len(grid), len(grid[0])
    visited = [[False]*m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                bfs_or_dfs(i, j, grid, visited)
                count += 1
    return count
```

### 2. 최단 거리 (레벨)
BFS + (노드, 거리) 튜플로 큐에 넣기.

### 3. 양방향 BFS
시작과 끝에서 동시에 BFS, 가운데서 만나면 종료. 2배 빨라짐.

### 4. 0-1 BFS
가중치가 0 또는 1인 그래프 → 일반 큐 대신 deque 사용. 가중치 0이면 `appendleft`, 1이면 `append`.

### 5. 멀티소스 BFS
시작점이 여러 개 (예: 토마토 익히기). 처음에 모든 시작점을 큐에 넣고 동시에 시작.

```python
q = deque()
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:    # 모든 시작점
            q.append((i, j, 0))
```

### 6. 백트래킹 (DFS의 변형)
조건 안 맞으면 되돌리기. N-Queen, 스도쿠 등.

## 풀이 사고 순서

1. 그래프인가 격자인가? (인접리스트 / dx,dy)
2. 최단 거리? → BFS / 모든 경로? → DFS
3. **방문 처리**는 어떻게? (set / 2D 배열 / 거리 배열)
4. 시작점 / 종료 조건 명확히
5. 큐/스택에 넣을 정보 정의 ((노드,) / (x,y,거리,...))

## 흔한 실수

- **방문 처리 누락** → 무한 루프 / 시간 초과
- 방문 처리를 **꺼낼 때**가 아니라 **넣을 때** 해야 함 (안 그러면 큐에 중복으로 쌓임)
- DFS 재귀 한도 — `sys.setrecursionlimit(10**6)`
- 격자 인덱스 범위 체크 (`0 <= nx < n`)
- BFS에서 거리 정보 누락 — 큐에 `(노드, 거리)` 같이 넣기

## 시간복잡도

| | 인접 리스트 | 인접 행렬 |
|---|---|---|
| BFS/DFS | O(V + E) | O(V²) |

V = 노드 수, E = 간선 수.

## 신호 — BFS / DFS 문제

- "**최단 거리**", "최소 이동", "최소 횟수" → BFS
- "방문 가능한 노드 수", "섬의 개수", "연결된 영역" → 둘 다
- "모든 경로", "모든 조합" → DFS / 백트래킹
- 격자 문제 (대부분)
- 그래프 + 탐색

## 실전 팁

- BFS는 **`deque` + `visited`** 두 줄이 핵심. 손에 익혀두기
- DFS는 재귀가 짧고 직관적, 깊이 깊으면 명시적 스택
- 격자는 `dx`, `dy` 방향 배열 외워두기 (4방향, 8방향)
- 시작점 큐에 넣을 때 **방문 처리 같이** 하기

## 다음으로
- **다익스트라** (`2순위_다익스트라.md`) — 가중치 그래프 BFS의 일반화
- **DP** (`2순위_DP.md`) — DFS + 메모이제이션
- **위상정렬** (`2순위_위상정렬.md`) — BFS 변형
