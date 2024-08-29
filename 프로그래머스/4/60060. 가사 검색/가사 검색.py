def solution(words, queries):
    
    # words : 가사에 사용된 모든 단어 
    # --> 2~100,000 개
    # --> 단어 길이의 합 : ~ 1,000,000
    
    # queries : 찾을 단어 
    # --> words : ~ 100,000개 이하 
    # --> 중복될 수도 있음 <-> 해당 결과값은 저장해두는게 빠름 
    
    # 완전탐색 <-> O(N^2) -> 시간 초과 
    # O(N) 또는 O(N log N)
    # O(N) 은 무조건 : queries는 하나씩 조회 
    
    # 검사 대상 : words , words의 문자열이 거꾸로 뒤집힌 배열 
    forward_words = [[] for _ in range(10001)]
    backward_words = [[] for _ in range(10001)] 
    
    # 순차 탐색 : O(N)
    for word in words : 
        le = len(word)
        forward_words[len(word)].append(word)
        backward_words[len(word)].append(word[::-1])
    
    # 정렬 : O(log N) * O(N)
    for i in range(1, 10001) : 
        forward_words[i].sort()
        backward_words[i].sort()
    
    answer = []
    
    # O(N)
    for query in queries :
        if query[0] != '?' : 
            # words 사용해 이분 탐색 
            # 범위 적용되는 가장 작은 index 
            # 가장 큰 index 
            # 빼서 반환 
            min_index = min_search(forward_words[len(query)], query) 
            max_index = max_search(forward_words[len(query)], query)
                       
        else : 
            # reversed words 사용해 이분 탐색 
            min_index = min_search(backward_words[len(query)], query[::-1]) 
            max_index = max_search(backward_words[len(query)], query[::-1])
        answer.append(max_index - min_index) 
        
    return answer

def min_search(words, query) : 
    # ["frodo", "front", "fr", "frozennnn", "frame", "kakao"]
    # 단어 길이로 1차 정렬, 알파벳 순으로 2차 정렬 
    
    query = query.replace("?","a")
    # freaa frezz --> 만약 'fre' 가 같은 단어가 없다면 둘 다 똑같은 index 나옴 --> 결국 0 반환 
    left , right = 0 , len(words) - 1 
    
    # "frame" , "frodo", "front", "frost"
    while left <= right : 
        mid = (left+right) // 2
        if words[mid] < query : 
            left = mid + 1 
        else : 
            right = mid - 1       
    return left 

def max_search(words, query) : 
    
    query = query.replace("?","z") 
    left, right = 0, len(words) - 1 
    
    while left <= right : 
        
        mid = (left+right) // 2
        if words[mid] > query : 
            right = mid - 1   
        else : 
            left = mid + 1 
                     
    return right + 1
    