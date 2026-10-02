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

# 학생들 번호는 체격순
# 바로 앞 번호의 학생 or 뒷 번호 학생에게만 빌려줄 수 있다.
# 최대한 많은 학생이 체육수업을 들어야한다. -> 그리디?

# 입력값 - n: 전체 학생 수, lost: 도난당한 학생들의 번호 리스트, reverse: 여벌의 체육복이 있는 학생들의 번호 리스트
# 출력값 - 체육복을 가지는 학생의 최댓값
# 2 <= n <= 30
# 1 <= len(reverse) <= n

# 그리디 -> 여분의 옷을 가진 학생의 앞 뒤에 없는 학생이 존재할때 무조건 주자. 매 순간 최댓값



