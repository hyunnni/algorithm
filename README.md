# 📘 알고리즘 문제 풀이

알고리즘 문제를 풀고 기록하는 저장소입니다.  

---

## 🚀 문제 정리
| 플랫폼 | 문제 번호 | 문제 이름 | 분류 | 풀이 코드 | 풀이 과정 |
|--------|---------|----------|------|------------|------------|
| 백준 | 1012 | [유기농 배추](https://www.acmicpc.net/problem/1012) | 그래프 탐색 (BFS/DFS) | [📂 BFS 풀이](problems/baekjoon/1012_bfs.py) / [📂 DFS 풀이](problems/baekjoon/1012_dfs.py) |  |
| 백준 | 1260 | [DFS와 BFS](https://www.acmicpc.net/problem/1260) | 그래프 탐색 (BFS/DFS) | [📂 코드](problems/baekjoon/1260.py) | |
| 백준 | 1261 | [알고스팟](https://www.acmicpc.net/problem/1261) | 그래프 탐색 (BFS) | [📂 코드](problems/baekjoon/1261.py) | [📄 풀이 과정](notes/baekjoon/1261.md) |
| 백준 | 1389 | [케빈 베이컨의 6단계 법칙](https://www.acmicpc.net/problem/1389) | 완전 탐색 | [📂 코드](problems/baekjoon/1389.py) |  |
| 백준 | 1697 | [숨바꼭질](https://www.acmicpc.net/problem/1697) | 그래프 탐색 (BFS) | [📂 코드](problems/baekjoon/1697.py) | |
| 백준 | 2178 | [미로 탐색](https://www.acmicpc.net/problem/2178) | 그래프 탐색 (BFS) | [📂 코드](problems/baekjoon/2178.py) |  |
| 백준 | 2206 | [벽 부수고 이동하기](https://www.acmicpc.net/problem/2206) | 그래프 탐색 (BFS) | [📂 코드](problems/baekjoon/2206.py) |  |
| 백준 | 2163 | [초콜릿 자르기](https://www.acmicpc.net/problem/2163) | 그리디 & 수학 | [📂 코드](problems/baekjoon/2163.py) |  |
| 백준 | 2309 | [일곱 난쟁이](https://www.acmicpc.net/problem/2309) | 완전 탐색 & 정렬 | [📂 코드](problems/baekjoon/2309.cpp) | |
| 백준 | 2468 | [안전 영역](https://www.acmicpc.net/problem/2468) | 그래프 탐색 (BFS) | [📂 코드](problems/baekjoon/2468.py) | |
| 백준 | 2587 | [안전 영역](https://www.acmicpc.net/problem/2587) | 수학 & 구현 | [📂 코드](problems/baekjoon/2587.cpp) | |

---


## 📌 기타 학습 자료
### 📖 알고리즘 개념 정리
- [BFS 개념 정리](notes/algorithms/bfs.md)
- [DFS 개념 정리](notes/algorithms/dfs.md)
- [Python 입력 처리 가이드](notes/coding-guides/python-input-guide.md)

---

### 📆 **목표**
✅ 문제 해결 과정 정리하기  
✅ 정리한 내용을 `notes/` 폴더에 추가하기  

---

## 📮 Git 커밋 메시지 스타일

### 📌 커밋 메시지 기본 규칙
- `type` (커밋 유형)
- `scope` (적용 범위)
- `메시지 요약` (어떤 작업을 했는지 간결히 설명)

---

#### `type` (커밋 유형)
| 타입 | 설명 | 예시 |
|------|----------------------------|---------------------------------|
| **feat** | 새로운 문제 풀이 추가 | `feat(baekjoon): Solve #1261 (BFS)` |
| **refactor** | 코드 리팩토링 (기능 변화 없음) | `refactor(#1261): Improve BFS logic` |
| **docs** | 문서 및 주석 추가 | `docs(#1261): Add comments for BFS` |
| **chore** | 폴더 구조 정리, 설정 변경 | `chore(notes): Restructure notes` |

---

#### `scope` (적용 범위)
| 범위 | 설명 | 예시 |
|------|-----------------|----------------------------------|
| **baekjoon** | 백준 문제 풀이 | `feat(baekjoon): Solve #1261 (BFS)` |
| **programmers** | 프로그래머스 문제 풀이 | `feat(programmers): Solve #178871` |
| **notes** | 학습 노트 정리 | `chore(notes): Restructure folders` |
| **docs** | 문서 추가 (주석, 개념 정리) | `docs(#1261): Add explanation for BFS` |

---

### 📌 커밋 메시지 작성 규칙
1. **커밋 메시지는 한 줄 요약을 기본으로 작성**  
2. **영어 소문자로 시작 (`feat`, `refactor`, `docs`, `chore`)**  
3. **문제 번호 포함 (`#1234`)**  

---

### 📌 정리 및 적용 예시
✅ **새로운 문제를 풀었을 때 → `feat` 사용**  
✅ **코드를 개선했을 때 → `refactor` 사용**  
✅ **주석이나 문서를 추가했을 때 → `docs` 사용**  
✅ **폴더 정리나 구조 변경 시 → `chore` 사용**  