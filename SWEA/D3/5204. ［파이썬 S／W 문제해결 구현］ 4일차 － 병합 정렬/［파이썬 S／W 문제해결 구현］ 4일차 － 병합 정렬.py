def msort(lst):
    global ANS

    # [1] 종료조건: 더 이상 절반을 나눠줄 개수가 아니라면
    if len(lst) < 2:
        return lst

    # [2] 단위작업 : 절반으로 나누어서 각가 정렬후([3] 재귀), 오름차순으로 합쳐서 리턴
    # [2-1] 절반으로 나눠서 정렬 : lst[:m], lst[m:]
    m = len(lst)//2 #  m까지..? m 전까지...? => 헷갈리면 적어보기
    left = msort(lst[:m])
    right = msort(lst[m:])

    # [2-2] 정렬된 두 리스트 합치기
    l = r = 0
    mlst = []
    while l<len(left) and r<len(right): # 둘중 하나가 소진된경우 탈출 
        if left[l] <= right[r]: # 왼쪽이 작거나 같은 경우 (최종 답이 오른쪽보다 클때만 count되기 때문에)
            mlst.append(left[l])
            l+=1
        else:
            mlst.append(right[r])
            r+=1

    if l < len(left): # 왼쪽이 남은 경우
        ANS+=1
        return mlst + left[l:]
    elif r < len(right) :
        return mlst + right[r:]
 #   return mlst + left[l:] + right[r:]


#    return mlst + left[l:] + right[r:] # 둘중하나는 빈리스트, 나머지는 정렬


TC = int(input())
for tc in range(1, TC+1) :
    N = int(input())
    A = list(map(int, input().split()))

    # lst = qsort(A)
    ANS = 0
    lst = msort(A)
    # print(lst)
    print(f'#{tc} {lst[N//2]} {ANS}')

