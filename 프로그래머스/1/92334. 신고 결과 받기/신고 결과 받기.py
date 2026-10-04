# k번 이상 신고: 정지 + 신고한 유저들에게 정지 사실 메일 발송
# 출력값: 각 유저별로 처리결과 메일을 받은 횟수를 배열로 return
def solution(id_list, report, k):
    # 신고 횟수 리스트
    report_count = [[0]*len(id_list) for i in range(len(id_list))]
    # 아이디를 인덱스로 변환하자
    id_to_index = {}
    # 중복 신고 체크
    check_duplication = set()
    # 정지 당한 사람
    ban_id = []
    # 이메일 리스트
    email_count = [0 for i in range(len(id_list))]
    
    
    for index, value in enumerate(id_list):
        id_to_index[value] = index
    
    # report를 순회하여 리포트 수 갱신
    for r in report:
        result = r.split()
        reporter = result[0]
        get_report = result[1]
        
        if (reporter, get_report) in check_duplication:
            continue
            
        check_duplication.add((reporter, get_report))
        
        report_count[id_to_index[reporter]][id_to_index[get_report]] += 1
        
    # 정지 id 갱신
    for i in range(len(report_count)):
        total = 0
        for j in range(len(report_count)):
            total += report_count[j][i]
        
        if total >= k:
            ban_id.append(i)
    
    # 메일 발송
    for id in ban_id:
        for index, p in enumerate(report_count):
            if p[id] > 0:
                email_count[index] += 1
                
    return email_count