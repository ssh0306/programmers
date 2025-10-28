def solution(strings, n):
    #결과값을 담을 리스트
    answer = []
    #정렬하기 위한 리스트
    n_strings = []
    
    for s in strings:
        #예시 n=1 일 때 ("u", "sun")
        #n_strings에 [("u", "sun"), ("e", "bed"), ("a", "car")]로 담기
        n_strings.append((s[n], s))
    
    #여기에서 정렬함
    n_strings.sort()
    
    #정렬된 n_string의 인덱스 1번만 answer에 담음
    for i in n_strings:
        answer.append(i[1])
    return answer