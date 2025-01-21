def solution(players, callings):
    
    rank_dic = {player : index for index, player in enumerate(players)}
    
    for cur_player in callings:
        
        cur_player_rank = rank_dic[cur_player]
        
        rank_dic[cur_player] -= 1
        rank_dic[players[cur_player_rank - 1]] += 1
        
        players[cur_player_rank-1], players[cur_player_rank] = players[cur_player_rank], players[cur_player_rank-1]

    return players
