def solution(tickets):
    answer = []
    tickets.sort()
    
    def dfs(cur, path):
        if len(path) == len(tickets) + 1:
            answer.extend(path)
            return True
        
        for i, (start,dest) in enumerate(tickets):
            if start == cur:
                tickets[i] = (None, None)
                if dfs(dest, path + [dest]):
                    return True
                tickets[i] = (start, dest)
        
        return False
    
    dfs("ICN", ["ICN"])
        
    return answer