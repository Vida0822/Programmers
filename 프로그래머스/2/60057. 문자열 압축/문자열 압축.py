def solution(S):
    # [0] 시뮬레이션 준비
    N = len(S)

    # debug = 0
    # print(S, N)

    # [1] 시뮬레이션 실행
    answer = 1000  # 최소 문자열 길이

    # 0) 자를 단위 정하고
    for k in range(1, N + 1):
        cnt = 1
        prev = ''
        new_S = ''
        # debug = 1
        # print(prev)
        # print(round(N / k))
        for i in range(N // k+2):
            # 1) 문자 추출
            cur = S[i * k:(i + 1) * k]
            # debug = 2
            # print(cur)

            # 2) 이전 문자 압축
            # print('bef',new_S)
            if prev == cur:
                cnt += 1
                # debug = 3
                # print(f"cnt={cnt}, prev={prev}, cur={cur}")

            else:
                if cnt > 1:
                    new_S += (str(cnt) + prev)
                elif cnt == 1:
                    new_S += prev
                cnt = 1
                prev = cur
                # debug = 4
                # print(new_S)

            # debug = 5
            # print('aft',new_S)

        # 4) min 갱신
        answer = min(answer, len(new_S))
        # debug = 6
        # print(answer, new_S, len(new_S))

    return answer
