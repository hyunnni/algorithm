# 🔍 백트래킹(Backtracking) 기초 개념 및 예제

## 📌 백트래킹이란?

백트래킹(Backtracking)은 **모든 가능한 경우의 수를 탐색**하면서, **불필요한 경로는 조기에 차단(가지치기, Pruning)** 하여 탐색 속도를 향상시키는 기법이다.

### ✅ 백트래킹의 핵심 원리
1. **재귀(DFS) 구조 활용** → 모든 경우의 수를 탐색.
2. **백트래킹(Backtrack)** → 탐색이 끝난 후 이전 상태로 되돌아가기.

---

## 🔹 백트래킹 함수 설계 과정

### ✅ 1. 문제를 "결정 문제(선택 or 비선택)" 형태로 변환
- 현재 요소를 선택할 것인가? 선택하지 않을 것인가?
- 예: **부분수열(1182번)** → 현재 숫자를 **선택하거나 선택하지 않음**

### ✅ 2. 종료 조건(Base Case) 설정
- 언제 탐색을 멈출 것인가?
- 예: 배열을 끝까지 탐색했을 때 (`idx == N`)

### ✅ 3. 탐색할 범위 설정
- 현재 단계에서 선택할 수 있는 요소는 무엇인가?
- 예: `idx` 번째 숫자를 선택하거나 선택하지 않음

### ✅ 4. 백트래킹(원상 복구) 적용
- 탐색이 끝난 후 상태를 복원해야 함
- 예: `total - arr[idx]`

---

## 🛠 코드 예제: 백준 1182 - 부분수열의 합

### 📌 문제 요약
배열에서 합이 `S`가 되는 **부분수열**의 개수를 찾는 문제.

### **✅ 해결 방법 (백트래킹 사용)**
1. **각 원소를 "선택"하거나 "선택하지 않는" 두 가지 경우를 탐색**
2. **부분수열의 합이 `S`가 되는 경우 count 증가**
3. **DFS(백트래킹)를 활용하여 모든 부분집합 탐색**

```python
import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
count = 0  # 합이 S가 되는 부분수열 개수

def backtrack(idx, total):
    global count

    # 종료 조건: 모든 원소를 확인했을 때
    if idx == N:
        return

    # 현재 원소를 선택한 경우
    total += arr[idx]  
    if total == S:  
        count += 1  # 조건 만족하면 count 증가

    backtrack(idx + 1, total)  # 다음 원소 탐색

    # 현재 원소를 선택하지 않는 경우 (백트래킹)
    backtrack(idx + 1, total - arr[idx])  # 원상 복구

backtrack(0, 0)
print(count)
```

---

## 🔹 백트래킹 호출 예시

### 🎯 **입력 예시**
```
N = 3, S = 3
arr = [1, 2, 3]
```

### **백트래킹 호출 트리**
```
backtrack(0, 0)
 ├─ backtrack(1, 1)   # 1을 선택
 │  ├─ backtrack(2, 3)   # 2를 선택 → S 만족!
 │  │  ├─ backtrack(3, X)  # 종료
 │  │  ├─ backtrack(3, X)  # 종료
 │  ├─ backtrack(2, 1)   # 2를 선택 안 함
 │     ├─ backtrack(3, 4)  # 3을 선택 → 종료
 │     ├─ backtrack(3, 1)  # 3을 선택 안 함 → 종료
 ├─ backtrack(1, 0)   # 1을 선택 안 함
    ├─ backtrack(2, 2)   # 2를 선택
    │  ├─ backtrack(3, 5)  # 3을 선택 → 종료
    │  ├─ backtrack(3, 2)  # 3을 선택 안 함 → 종료
    ├─ backtrack(2, 0)   # 2를 선택 안 함
       ├─ backtrack(3, 3)  # 3을 선택 → S 만족!
       ├─ backtrack(3, 0)  # 3을 선택 안 함 → 종료
```

---