##특정 문자 제거하기 
def solution(my_string, letter):
    answer = my_string.replace(letter, '')
    return answer

##각도기 
def solution(angle):
    answer = 0
    if (angle > 0) & (angle < 90):
        answer = 1
    elif (angle == 90):
        answer = 2
    elif (angle > 90) & (angle < 180):
        answer = 3
    else: 
        answer = 4 
    return answer

##양꼬치 
def solution(n, k):
    free_drinks = n // 10
    answer = (n * 12000) + ((k - free_drinks) * 2000)
    return answer

##짝수의 합
def solution(n):
    answer = 0
    while n > 0:  
        if n % 2 == 0:  
            answer += n
        n -= 1  
    return answer

##another solution
def solution(n):
    answer = 0
    for i in range(2, n+1, 2):
        answer += i
    return answer