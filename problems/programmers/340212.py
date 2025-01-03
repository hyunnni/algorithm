def time_to_solve(level, diff, cur_time, prev_time):
    if level >= diff:
        return cur_time
    else:
        return (cur_time + prev_time) * (diff - level) + cur_time


def solution(diffs, times, limit):
    
    #총 시간
    time_sum = 0
    
    #숙련도
    min_level, max_level = 1, max(diffs)
    
    
    while min_level < max_level:
        
        mid_level = (min_level + max_level) // 2
        mid_total = 0
        
        for i in range(len(diffs)):
            
            if not i:
                prev_time = 0
            else:
                prev_time = times[i-1]

            cur_time = times[i]		# 현재 문풀 시간
            mid_total += time_to_solve(mid_level, diffs[i], cur_time, prev_time)
            
        if mid_total <= limit:
            max_level = mid_level
        else:
            min_level = mid_level + 1
                

    return min_level