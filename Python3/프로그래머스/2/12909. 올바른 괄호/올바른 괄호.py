def solution(s):
    #스택을 활용해서 각각의 괄호가 짝짓는지 확인하기
    stack = []
    stack.append(s[0])
    #')'로 시작하는 경우는 무조건 false
    if s[0] == ')':
        return False
    else:
    #아니라면 그 다음 괄호 검사
        for i in s[1:]:
            #짝 지어지면 pop
            if stack and stack[-1] == '(' and i == ')':
                stack.pop()
            else:
            #짝 지어지지 않으면 다음 단계로 넘어가 짝 지어지는지 확인하기
                stack.append(i)
                
    #stack에 들어 있는 게 없으면 모두 짝 지어진 것
    if len(stack) == 0:
        return True
    #stack에 남아 있으면 짝 지어지지 못한 게 있는 것
    else:
        return False