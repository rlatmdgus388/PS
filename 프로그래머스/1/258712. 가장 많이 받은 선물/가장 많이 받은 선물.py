# 주고 받은 선물 o:
#   더 많이 준 사람이 받음
# 주고 받은 선물 x or 선물 수 같음:
#   선물지수 더 큰 사람이 받음
#   선물지수도 같으면 x
# 선물지수 = 준 선물 수 - 받은 선물 수

def solution(friends, gifts):
    friends_gift_dic = {}
    friends_gift_rate_dic = {}
    will_get_gift_dic = {}
    max_count = 0

    for friend in friends:
        friends_gift_dic[friend] = {}
        will_get_gift_dic[friend] = 0
        friends_gift_rate_dic[friend] = 0

        for f in friends:
            if f == friend:
                continue

            friends_gift_dic[friend][f] = 0

    # 선물 이력 반영
    for gift in gifts:
        give, take = gift.split()

        friends_gift_dic[give][take] += 1

    # 선물 지수 반영
    for friend1 in friends_gift_dic:
        for friend2 in friends_gift_dic[friend1]:

            friend1_give = friends_gift_dic[friend1][friend2]
            friend2_give = friends_gift_dic[friend2][friend1]

            friends_gift_rate_dic[friend1] += friend1_give - friend2_give

    # 받을 선물 계산
    checked = set()

    for friend1 in friends_gift_dic:

        for friend2 in friends_gift_dic[friend1]:

            # 이미 비교한 쌍이면 넘어감
            if (friend1, friend2) in checked or (friend2, friend1) in checked:
                continue

            checked.add((friend1, friend2))

            friend1_give = friends_gift_dic[friend1][friend2]
            friend2_give = friends_gift_dic[friend2][friend1]

            friend1_rate = friends_gift_rate_dic[friend1]
            friend2_rate = friends_gift_rate_dic[friend2]

            # 주고 받은 선물 x
            if friend1_give == 0 and friend2_give == 0:

                if friend1_rate > friend2_rate:
                    will_get_gift_dic[friend1] += 1

                elif friend1_rate < friend2_rate:
                    will_get_gift_dic[friend2] += 1

            # 주고 받은 선물 o
            else:

                # 더 많이 준 사람이 받음
                if friend1_give > friend2_give:
                    will_get_gift_dic[friend1] += 1

                elif friend1_give < friend2_give:
                    will_get_gift_dic[friend2] += 1

                # 주고받은 수가 같으면 선물지수 비교
                else:

                    if friend1_rate > friend2_rate:
                        will_get_gift_dic[friend1] += 1

                    elif friend1_rate < friend2_rate:
                        will_get_gift_dic[friend2] += 1

    # 최댓값
    for value in will_get_gift_dic.values():
        if value > max_count:
            max_count = value

    return max_count