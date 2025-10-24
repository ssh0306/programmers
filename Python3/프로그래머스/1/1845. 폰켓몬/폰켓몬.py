def solution(nums):
    ponketmon = dict()
    
    #홍박사가 가지고 있는 총 폰켓몬의 수
    N = len(nums)
    #선택 가능한 폰켓몬의 최대 수 
    K = N // 2
    
    #홍박사가 보유하고 있는 폰켓몬의 종류 구하기
    for n in nums:
        if n in ponketmon:
            ponketmon[n] += 1
        else:
            ponketmon[n] = 1
            
    #최대 선택할 수 있는 폰켓몬의 수 구하기
    #선택한 폰켓몬 수가 전체 폰켓몬 수보다 적을 때
    # len(ponketmon) 홍박사가 가진 폰켓몬의 종류의 수, 즉 key의 수 
    if K <= len(ponketmon):
        return K
    else:
        return len(ponketmon)