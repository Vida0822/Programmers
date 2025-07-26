N = int(input())  # N <= 10억 --> O(N)

# 방번호 N , 층 수 cnt (:건너가는 개수, 즉 anw)
# N = 1 + 6 + 6x2 + ... + 6x(cnt-1) 
# --> 나눠서 cnt 를 구하는건 다항식이라 어려움 , 곱하기로 더해가며 값이 나올때까지 비교
i = 1 
cnt = 1 
while i < N : 
    i += cnt*6 
    cnt += 1   
print(cnt) 
    
    