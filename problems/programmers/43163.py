from collections import deque

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    def bfs():
        queue = deque([(begin,0)])
        visited = set()
        visited.add(begin)
        
        while queue:
            cur_word, step = queue.popleft()
            
            if cur_word == target:
                return step
            
            for word in words:
                if diff(cur_word, word) and word not in visited:
                    queue.append((word, step+1))
                    visited.add(word)
        return 0
    
    return bfs()

def diff(str1, str2):
    diff_cnt = sum(1 for a,b in zip(str1, str2) if a!= b)
    return diff_cnt == 1