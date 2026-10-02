# 스택 활용
# 바구니 관리를 어떻게 할까
#   1. 기준을 항상 스택의 top을 기준으로 하자.
#   2. 탑 > 0인 경우 탑 -1과 매번 비교하여 같으면 둘 다 pop
def solution(board, moves):
    # 바구니
    basket = []
    
    # 터뜨려져 사라진 인형의 개수
    num = 0
    
    # 인형 뽑기
    for move in moves:
        for row in board:
            if row[move - 1] != 0:
                basket.append(row[move - 1])
                
                if len(basket) > 1:
                    if basket[-1] == basket[-2]:
                        basket.pop()
                        basket.pop()
                        num += 2
                
                row[move - 1] = 0
                break
            else:
                continue
    
    
    return num