## 문자열 뒤집기 
def solution(my_string):
    answer = ''.join(reversed(my_string))
    return answer 

# other solution
def solution(my_string):
    answer = my_string[::-1]
    return answer

# .join(): 문자열 리스트 또는 iterable을 '하나의 문자열'로 결합할 때 사용 
