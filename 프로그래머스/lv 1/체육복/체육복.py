def solution(n, lost, reserve):
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)

    for i in sorted(reserve):
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)

    answer = n - len(lost)

    return answer