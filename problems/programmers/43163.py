from collections import deque

def solution(begin, target, words):
    
    # target이 words에 없으면 0
    if target not in words:
        return 0
    
    # BFS 함수 정의 
    def bfs():
        queue = deque([(begin,0)]) # (현재 단어, 변환 단계)
        visited = set() # 방문한 단어를 저장
        visited.add(begin)
        
        while queue:
            cur_word, step = queue.popleft()
            
            # 현재 단어가 target이면 변환 단계를 반환
            if cur_word == target:
                return step
            
            # words를 순회하며 변환 가능한 단어 탐색
            for word in words:
                if diff(cur_word, word) and word not in visited:
                    queue.append((word, step+1))
                    visited.add(word)
                    
        return 0    # 변환 불가 경우
    
    return bfs()

def diff(str1, str2):
    # 두 단어의 다른 문자 개수 세기
    diff_cnt = sum(1 for a,b in zip(str1, str2) if a!= b)
    return diff_cnt == 1