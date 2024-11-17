## 문자열 뒤집기 
def solution(my_string):
    answer = ''.join(reversed(my_string))
    return answer 

# other solution
def solution(my_string):
    answer = my_string[::-1]
    return answer

# .join(): 문자열 리스트 또는 iterable을 '하나의 문자열'로 결합할 때 사용

## 직각삼각형 출력하기 
n = int(input())

def print_triangle(n):

    for i in range(1, n + 1):
        print('*' * i)    

print_triangle(3)

# 피타고라스 정리 활용

## 짝수 홀수 개수를 담은 배열 
def solution(num_list):
    answer = []
    pair_count = 0
    odd_count = 0

    for i in num_list:
        if i % 2 == 0:
            pair_count += 1
        else: 
            odd_count += 1
    answer = [pair_count, odd_count]

    return answer 

# other solution 
def solution(num_list):
    answer = [0,0]

    for num in num_list:
        if num % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1

    return answer

## 문자 반복 출력하기 
def solution(my_string, n):
    answer = ''

    for i in my_string:
        str = (i * n)
        answer += str
    return answer

solution('hello', 3)

# other solution 
def solution(my_string, n):
    return ''.join(i*n for i in my_string)


