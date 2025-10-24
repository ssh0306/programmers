def solution(arr):
    #answer에 arr에 있는 수를 비교한 후 넣기
    #arr[0]부터 넣어보기
    answer = [arr[0]]
    
    #arr[1]부터 마지막까지 answer = [arr[0]]와 비교하기
    for i in range(1, len(arr)):
        #i번째 숫자가 그 다음으로 넣은 숫자랑 다르면 넣기
        if arr[i] != answer[-1]:
            answer.append(arr[i])
    return answer