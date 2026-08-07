def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    for city in cities:
        if city.lower() in cache:
            cache.remove(city.lower())
            cache.append(city.lower())
            answer += 1
        else:
            if len(cache) < cacheSize:
                cache.append(city.lower())
            elif len(cache) == cacheSize & len(cache) != 0:
                cache.pop(0)
                cache.append(city.lower())
            answer += 5
    return answer