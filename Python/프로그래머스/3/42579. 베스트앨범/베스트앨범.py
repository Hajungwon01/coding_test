def solution(genres, plays):
    answer = []
    tmp = dict()
    sum_genre = dict()
    
    for i in range(len(genres)):
        sum_genre[genres[i]] = sum_genre.get(genres[i], 0) + plays[i]
        if genres[i] not in tmp.keys():
            tmp[genres[i]] = [(plays[i], i)]
        else:
            tmp[genres[i]].append((plays[i], i))
            
    sorted_genres = sorted(sum_genre.items(), key=lambda x: x[1], reverse=True)
    for g in sorted_genres:
        tmp[g[0]].sort(key=lambda x: (-x[0], x[1]))
        top_songs = tmp[g[0]][:2]
        
        answer += [song[1] for song in top_songs]
        
        
    return answer