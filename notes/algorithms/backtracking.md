# 🔍 백트래킹(Backtracking) 기초 개념 및 예제

## 📌 백트래킹이란?

백트래킹(Backtracking)은 **모든 가능한 경우의 수를 탐색**하면서, **해가 될 수 없다고 판단되면 되돌아가 해를 다시 찾아가는 기법**이다.

### ✅ 백트래킹의 핵심 과정
1. **재귀(DFS) 구조 활용** → 모든 경우의 수를 탐색.
2. **가지치기(Pruning)** → 불필요한 탐색을 조기에 종료하여 속도 향상.
3. **백트래킹(Backtrack)** → 탐색이 끝난 후 이전 상태로 되돌아가기.

---

## 🛠 코드 예제: 백준 15649 - N과 M (1)

### 📌 문제 요약
1부터 N까지의 숫자 중에서 **M개를 중복 없이 선택**하여 모든 순열을 출력하는 문제.

### **✅ 해결 방법 (백트래킹 사용)**
1. **DFS(재귀 함수)로 모든 경우 탐색**.
2. **방문한 숫자는 다시 선택하지 않도록 `visited` 리스트 사용**.
3. **M개를 선택한 경우 출력 후 백트래킹(원상 복구).**

```python
import sys

N, M = map(int, sys.stdin.readline().split())
visited = [False] * (N + 1)
result = []

def backtrack(depth):
    if depth == M:  # M개 선택 완료
        print(*result)
        return
    
    for i in range(1, N + 1):
        if not visited[i]:  # 방문하지 않은 숫자만 선택
            visited[i] = True
            result.append(i)
            backtrack(depth + 1)
            result.pop()  # 백트래킹 (원상복구)
            visited[i] = False

backtrack(0)
```

---

## 🔹 백트래킹 실행 흐름

### 🛠 **Step 1: 숫자 선택 (DFS 탐색)**
- `1 ~ N`까지의 숫자를 반복하면서 선택.
- 방문한 숫자는 `visited[i] = True`로 표시.

### 🛠 **Step 2: 종료 조건 (Base Case)**
- `M개`를 선택하면 출력하고 재귀 종료.

### 🛠 **Step 3: 백트래킹 (원상 복구)**
- 탐색이 끝난 후 마지막 숫자를 제거 (`pop()`).
- `visited[i] = False`로 방문 상태를 해제하여 다음 탐색 가능.

---

## 🚀 실행 예시

### **입력 예시**
```
3 2
```

### **실행 과정**
```
backtrack(0) → 초기 상태
```
1️⃣ **첫 번째 숫자 선택** (`i = 1`)
```
result = [1]
visited = [False, True, False, False]
backtrack(1) 호출
```
2️⃣ **두 번째 숫자 선택** (`i = 2`)
```
result = [1, 2]
visited = [False, True, True, False]
backtrack(2) 호출 → 출력: 1 2
백트래킹 (이전 상태로 복귀)
```
3️⃣ **다른 숫자로 탐색 진행**
```
1 3
2 1
2 3
3 1
3 2
```

### **최종 출력**
```
1 2
1 3
2 1
2 3
3 1
3 2
```

---