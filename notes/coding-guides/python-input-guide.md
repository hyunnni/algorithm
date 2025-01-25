# Python Input Functions and Usage

## `input()`

### 기능
- 표준 입력으로 한 줄을 입력받는다

### 특징
- 문자열 형태로 입력
- 입력 크기가 작거나 한 줄씩 처리할 때 적합

### 예
```python
n = int(input()) # 한 줄에서 정수 입력받기
array = list(map(int, input().split())) # 한 줄에서 공백으로 구분된 점수를 리스트로 입력받기 
```
<br>


## `sys.stdin.readline()`
### 기능
- 표준 입력에서 한 줄을 빠르게 읽어온다
### 특징
- **입력 크기가 크거나 많은 줄을 처리**할 때 효율적
- 입력받은 문자열 끝에 개행 문자 `\n`이 포함되므로 필요 시 `strip()`으로 제거 (int 형변환으로도 제거 가능)
### 예
```python
import sys
n = int(sys.stdin.readline().strip()) # 한 줄에서 정수 입력
array = list(map(int, sys.stdin.readline().split())) # 공백으로 구분된 정수 리스트 입력
```
<br>

## `strip()`
### 기능
- 문자열의 양쪽에서 특정 문자(공백, 개행 문자) 제거
### 특징
- `sys.stdin.readline()` 처럼 개행 문자가 포함된 입력에서 **개행 문자 제거**에 자주 사용
- 입력 문자열의 앞뒤에 있는 불필요한 공백 제거
### 예
```python
s = "   hello world  \n"
print(s.strip())    # 'hello world'
```

<br>

## `split()`
### 기능
- 문자열을 공백(또는 구분자) 기준으로 나누어 **리스트**로 변환
### 특징
- 기본적으로 공백으로 나누되, 구분자를 지정할 수 있다
- 여러 값이 한 줄에 입력될 때 유용
### 예
```python
s = "10 20 30"
array = list(map(int, s.split()))   # [10, 20, 30]

s = "apple,banana,cherry"
fruits = s.split(",")   # ['apple', 'banana', 'cherry']
```

## `map()`
### 기능
- **반복 가능한 객체**의 모든 요소에 대해 지정된 함수를 적용, 결과를 반환
### 특징
- 입력받은 문자열을 특정 타입(예:`int`)으로 변환할 때 유용
### 예
```python
array = list(map(int, input().split())) # 공백으로 구분된 정수 입력을 리스트로 변환
```
<br>

## List Comprehension
### 기능
- 간결하게 리스트 생성
### 특징
- 여러 줄의 입력을 리스트로 저장하거나, 조건에 따라 필터링할 시 유용
### 예
```python
# n줄의 문자열 입력을 리스트로 저장
n = 3
arr = [input() for _ in range(n)]

# n줄의 공백으로 구분된 정수 입력
arr = [list(map(int, input().split())) for _ in range(n)]
```
<br>

## `join`
### 기능
- 리스트나 튜플의 요소를 특정 문자열로 연결하여 하나의 문자열로 만든다
### 특징
- 리스트를 출력하거나 특정 형식으로 변환할 때 유용
### 예
```python
arr = ['a', 'b', 'c']
result = "-".join(arr)  # 'a-b-c'
```
<br>

## 활용예 정리
### 공백으로 구분된 정수 리스트로 입력받기
```python
array = list(map(int, input().split()))
```

### 여러 줄의 입력을 리스트로 저장하기
```python
import sys
n = int(input())
lines = [sys.stdin.readline().strip() for _ in range(n)]
```

### 2차원 배열 입력받기
```python
n, m = map(int, input().split())
matrix = [list(map(int, input().split)) for _ in range]
```

### 큰 입력을 빠르게 처리
```python
import sys
n = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().split()))
```
<br>

## 입력 상황에 따른 예

|상황|방식|
|------|---|
|입력 크기가 작음|`input()`|
|입력 크기가 큼|`sys.stdin.readline()`|
|여러 값이 한 줄에 공백으로 구분|`map(int,input().split())`|
|여러 줄을 입력받아야 함|`sys.stdin.readline()`|
|입력값 처리 필요 시|`strip()`, `split()`, `join` 등|