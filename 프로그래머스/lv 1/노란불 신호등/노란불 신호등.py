import math

def solution(signals):
	# 각 신호등 주기
	periods = [sum(signal) for signal in signals]
	# 전체 신호 패턴이 다시 반복되는 주기
	cycle = math.lcm(*periods)
	
	for t in range(cycle):
		is_yellow = True
		
		for i, p in enumerate(periods):
			yellow_start = signals[i][0]
			yellow_end = signals[i][0] + signals[i][1]
			
			current = t % p
			
			if not (yellow_start <= current < yellow_end):
				is_yellow = False
				break
				
		if is_yellow:
			return t
			
		return -1