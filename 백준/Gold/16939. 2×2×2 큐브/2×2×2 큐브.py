import copy

def left(cube, S):
    cp_cube = copy.deepcopy(cube)

    t1, t2 = cp_cube[13+S], cp_cube[14+S]
    cp_cube[13+S], cp_cube[14+S] = cp_cube[5+S], cp_cube[6+S]  # C <- D
    cp_cube[5+S], cp_cube[6+S] = cp_cube[17+S], cp_cube[18+S]  # D <- E
    cp_cube[17+S], cp_cube[18+S] = cp_cube[21+S], cp_cube[22+S]  # E <- F
    cp_cube[21+S], cp_cube[22+S] = t1, t2

    return cp_cube

def right(cube, S):
    cp_cube = copy.deepcopy(cube)

    t1, t2 = cp_cube[21+S], cp_cube[22+S]
    cp_cube[21+S], cp_cube[22+S] = cp_cube[17+S], cp_cube[18+S]  # E -> F
    cp_cube[17+S], cp_cube[18+S] = cp_cube[5+S], cp_cube[6+S] # D -> E
    cp_cube[5+S], cp_cube[6+S] = cp_cube[13+S], cp_cube[14+S] # C -> D
    cp_cube[13+S], cp_cube[14+S] = t1, t2  # F -> C

    return cp_cube

def up(cube, S):
    cp_cube = copy.deepcopy(cube)

    t1, t2 = cp_cube[24-S], cp_cube[22-S]  # F
    cp_cube[24 - S], cp_cube[22 - S] =  cp_cube[1 + S], cp_cube[3 + S] # F <- A
    cp_cube[1 + S], cp_cube[3 + S] = cp_cube[5+S], cp_cube[7+S] # A <- D
    cp_cube[5+S], cp_cube[7+S] = cp_cube[9 + S], cp_cube[11 + S]# D <- B
    cp_cube[9 + S], cp_cube[11 + S] = t1, t2  # B <- F

    return cp_cube


def down(cube, S):
    cp_cube = copy.deepcopy(cube)

    t1, t2 = cp_cube[24-S], cp_cube[22-S]  # F
    cp_cube[24 - S], cp_cube[22 - S] =  cp_cube[9+S], cp_cube[11+S] # F <- B
    cp_cube[9 + S], cp_cube[11 + S] = cp_cube[5+S], cp_cube[7+S] # B <- D
    cp_cube[5+S], cp_cube[7+S] = cp_cube[1 + S], cp_cube[3 + S] # D <- A
    cp_cube[1 + S], cp_cube[3 + S] = t1, t2  # A <- F

    return cp_cube

def left_front(cube, V, R, I):
    cp_cube = copy.deepcopy(cube)

    # 안쪽
    t = cp_cube[I]
    cp_cube[I] = cp_cube[I+1]
    cp_cube[I+1] = cp_cube[I+3]
    cp_cube[I+3] = cp_cube[I+2]
    cp_cube[I+2] = t

    # 바깥쪽
    t1, t2 = cp_cube[13+V], cp_cube[15+V]
    cp_cube[13 + V], cp_cube[15 + V] = cp_cube[2+R], cp_cube[1+R]
    cp_cube[1 + R], cp_cube[2 + R] = cp_cube[18 - V], cp_cube[20 - V]
    cp_cube[18 - V], cp_cube[20 - V] = cp_cube[12-R], cp_cube[11-R]
    cp_cube[12 - R], cp_cube[11 - R] = t1, t2

    return cp_cube


def right_front(cube, V, R, I):
    cp_cube = copy.deepcopy(cube)

    # 안쪽
    t = cp_cube[I]
    cp_cube[I] = cp_cube[I+2]
    cp_cube[I+2] = cp_cube[I+3]
    cp_cube[I+3] = cp_cube[I+1]
    cp_cube[I+1] = t

    # 바깥쪽
    t1, t2 = cp_cube[13+V], cp_cube[15+V] # C
    cp_cube[13+V], cp_cube[15+V] = cp_cube[11-R], cp_cube[12-R]
    cp_cube[11-R], cp_cube[12-R] = cp_cube[20-V], cp_cube[18-V]
    cp_cube[18-V], cp_cube[20-V]=  cp_cube[1+R], cp_cube[2+R]
    cp_cube[1+R], cp_cube[2+R] = t2, t1

    return cp_cube



def check(cp_cube):
    if not (cp_cube[1] == cp_cube[2] == cp_cube[3] ==cp_cube[4]):
        return False
    if not (cp_cube[5] == cp_cube[6] == cp_cube[7] ==cp_cube[8]):
        return False
    if not (cp_cube[9] == cp_cube[10] == cp_cube[11] ==cp_cube[12]):
        return False
    if not (cp_cube[13] == cp_cube[14] == cp_cube[15] ==cp_cube[16]) :
        return False
    if not (cp_cube[17] == cp_cube[18] == cp_cube[19] ==cp_cube[20]) :
        return False
    if not (cp_cube[21] == cp_cube[22] == cp_cube[23] ==cp_cube[24]) :
        return False

    return True



# MAIN
cube = [0]+list(map(int, input().split()))

# 8번 회전
if check(left(cube, 0)) or check(left(cube, 2)):
    print(1)
elif check(right(cube, 0)) or check(right(cube, 2)):
    print(1)
elif check(up(cube, 0)) or check(up(cube, 1)) :
    print(1)
elif check(down(cube, 0)) or check(down(cube, 1)):
    print(1)
elif check(left_front(cube, 0, 0, 21)) or check(left_front(cube, 1, 2, 5)):
    print(1)
elif check(right_front(cube, 0, 0, 21)) or check(right_front(cube, 1, 2, 5)):
    print(1)
else:
    print(0)
