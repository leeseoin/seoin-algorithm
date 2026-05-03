# DP (동적 계획법, Dynamic Programming)

## 한 줄 요약
**같은 부분 문제가 반복될 때, 한 번 계산한 결과를 저장해두고 재활용**하는 기법. 완전탐색의 진화형. "DP의 D는 Dynamic이지만 사실은 *Don't Repeat*".

## 직관 — 피보나치로 시작

```python
# 완전탐색 (지수 시간)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)
```

`fib(40)`만 해도 수십 초. 왜? `fib(38)`을 두 번, `fib(37)`을 세 번, ... 같은 걸 무한히 반복.

```python
# DP (선형 시간)
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)
```

데코레이터 한 줄로 **각 n에 대해 한 번만 계산**. 0.001초.

## DP를 쓸 수 있는 조건 2가지

### 1. 최적 부분 구조 (Optimal Substructure)
**큰 문제의 답을 작은 문제의 답으로 만들 수 있어야** 함.
- 최단 경로: A→C 최단 = (A→B 최단) + (B→C 최단)
- 피보나치: f(n) = f(n-1) + f(n-2)

### 2. 중복되는 부분 문제 (Overlapping Subproblems)
같은 부분 문제가 **여러 번 등장**.
- 안 그러면 메모이제이션이 의미 없음 (분할 정복으로 충분)

## 두 가지 구현 방식

### Top-down (메모이제이션, 재귀)
"필요할 때 계산하고 저장". 자연스러운 재귀 + `lru_cache`.

```python
@lru_cache(maxsize=None)
def solve(n):
    if 베이스: return 값
    return 점화식(solve(n-1), solve(n-2), ...)
```

**장점**: 사고가 자연스러움 (완탐 + 캐시), 필요한 것만 계산
**단점**: 재귀 깊이 한계, 함수 호출 오버헤드

### Bottom-up (반복문, 테이블)
"작은 것부터 차례로 채워나감". 배열에 채워가기.

```python
dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
return dp[n]
```

**장점**: 빠름, 재귀 한계 없음
**단점**: 점화식과 채우는 순서 정확히 알아야 함

## 점화식 사고법

DP의 핵심 = **점화식 세우기**.

### 1. 상태 정의
"`dp[i]`가 뭘 의미하는가?" 를 한국어로 쓰기.

> `dp[i] = i번째까지 봤을 때 만들 수 있는 최대 합`

### 2. 점화식 세우기
"어떻게 작은 것에서 큰 것으로 가는가?"

> `dp[i] = max(dp[i-1] + arr[i], arr[i])`

### 3. 베이스 케이스
> `dp[0] = arr[0]`

### 4. 답 위치
> `max(dp)` 또는 `dp[n-1]`

## 대표 DP 유형

### 1차원 DP

#### 계단 오르기
한 번에 1칸 또는 2칸. n번째 계단까지 가는 방법 수.
```python
dp[i] = dp[i-1] + dp[i-2]
```

#### 최대 부분합 (Kadane's algorithm)
연속한 부분배열의 최대 합.
```python
dp[i] = max(dp[i-1] + arr[i], arr[i])
```

#### 도둑 문제
인접한 집은 못 털 때 최대 금액.
```python
dp[i] = max(dp[i-1], dp[i-2] + arr[i])
```

### 2차원 DP

#### 격자 경로
(0,0)에서 (n,m)까지 오른쪽/아래만 가는 경우의 수.
```python
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

#### LCS (최장 공통 부분수열)
두 문자열의 공통 subsequence 중 가장 긴 것.
```python
if s1[i] == s2[j]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

### 배낭 문제 (Knapsack)

#### 0-1 배낭 (각 물건 0개 또는 1개)
```python
for i in range(1, n+1):
    for w in range(W+1):
        if weight[i] <= w:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i]] + value[i])
        else:
            dp[i][w] = dp[i-1][w]
```

#### 무한 배낭 (각 물건 무한 개)
```python
for i in range(1, n+1):
    for w in range(weight[i], W+1):
        dp[w] = max(dp[w], dp[w-weight[i]] + value[i])
```

## 완탐 → DP 사고 패턴

1. **일단 완탐으로 풀어보기** (재귀)
2. 같은 인자로 호출이 반복되는지 확인
3. 반복되면 → `@lru_cache` 추가 (Top-down DP 완성)
4. 더 빠르게? → Bottom-up으로 변환

## 풀이 사고 순서

1. **n이 작은가?** → 완탐 가능한지 먼저 봄
2. **선택의 연속**인가? → DP 의심
3. **상태 정의**: `dp[i] = ?` 를 한국어로
4. **점화식**: `dp[i] = f(dp[i-1], dp[i-2], ...)`
5. **베이스 케이스** + **답 위치**
6. Top-down vs Bottom-up 선택

## 신호 — DP 문제

- "**최대 / 최소**", "경우의 수"
- "**선택의 연속**" (각 단계마다 결정)
- "**한 번 본 건 다시 안 봄**" 같은 느낌
- 완탐으로 풀려고 하니 **2^n / n!** 폭발
- "i번째까지 ~한 결과" 같은 자연스러운 부분 문제

## 흔한 실수

- 점화식 잘못 세움 (특히 베이스 케이스)
- 인덱스 범위 (`dp[i-1]` 접근 시 `i >= 1`)
- 초기값 0이 아니어야 하는 경우 (`-inf`로 시작해야 할 때 등)
- 재귀 깊이 → `sys.setrecursionlimit(10**6)`

## 실전 팁

- **종이에 점화식 적기** — 머리로만 짜지 말 것
- 작은 케이스 손으로 dp 배열 채워보기
- Top-down으로 일단 돌아가게 만들고, 시간 부족하면 Bottom-up
- `lru_cache`는 인자가 hashable이어야 (리스트는 튜플로)

## 대표 문제 유형

- 계단 오르기, 1로 만들기, 정수 삼각형
- 등굣길, 가장 긴 증가하는 부분수열 (LIS)
- 배낭 문제, 동전 거스름돈
- 외판원 순회 (TSP, 비트마스크 DP)

## 다음으로
- **다익스트라** (`2순위_다익스트라.md`) — DP의 그래프 버전
- **이분탐색** (`2순위_이분탐색.md`) — 다른 최적화 기법
