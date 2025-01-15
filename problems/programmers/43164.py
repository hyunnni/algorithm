def solution(tickets):
    answer = []
    tickets.sort() # 정렬(알파벳순)
    
    def dfs(cur, path):
        if len(path) == len(tickets) + 1:
            answer.extend(path) # 경로 저장
            return True
        
        for i, (start,dest) in enumerate(tickets):
            if start == cur:    # 현재 도시에서 출발 가능한 경우
                tickets[i] = (None, None)   # 티켓 사용 표시
                if dfs(dest, path + [dest]):    # 다음 도시로 이동
                    return True
                tickets[i] = (start, dest)  # 티켓 복원(백트래킹)
        
        return False
    
    dfs("ICN", ["ICN"])
        
    return answer