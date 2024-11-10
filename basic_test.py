## 피자 나눠 먹기
import math 

def pizza_divide(n):
    pizza = 7
    answer = math.ceil(n / pizza)
    return answer

print(pizza_divide(5))

# round(1.4286)는 1로 반올림하므로, 피자가 한 판만 필요하다고 계산함. 하지만 7조각으로는 10명을 만족시킬 수 없기 때문에 이는 틀린 계산 

# ceil(1.4286)를 사용하면 2로 올림되므로, 피자 두 판이 필요하다고 정확히 계산

def solution(n):
    answer = 0

    if (n%7) == 0:
        answer = int(n/7)
    else:
        answer = int(n/7)+1

    return answer

## 피자 나눠 먹기 (2) 
import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def div_pizza2(n):
    if 1 <= n <= 100:
        return lcm(6, n) // 6
            
# 최소공배수 함수 (Least Common Multiple) 
def lcm(a, b):
    max_num = max(a, b)
    while True:
        if max_num % a == 0 and max_num % b == 0:
            return max_num 
        max_num += 1 

# other lcm function 
import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b) # gcd(Greatest, Common Divisor, 최대공약수)

## 피자 나눠 먹기 (3)
def div_pizza3(slice, n):
    return (n + slice - 1) // slice

# (n + divisor - 1) // divisor는 자동으로 올림이 되는 공식

# other solutions
from math import ceil

def solution(slice, n):
    return ceil(n / slice)

# another solutions
def solution(slice, n):
    answer = 0

    if n % slice != 0:
        answer = (n // slice) + 1
    else:
        answer = n // slice

    return answer

## 배열의 평균값
def solution(numbers):
    answer = 0
    sum = 0

    for n in numbers:
        sum += n
        answer = sum / len(numbers)
    return answer 

# other solution
import numpy as np

def solution(numbers):
    return np.mean(numbers)

# another solution 
def solution(numbers):
    return sum(numbers) / len(numbers)

## 옷가게 할인 받기 
def solution(price):
    answer = 0
    
    if price >= 500000:
        answer = price * 0.8
    elif price >= 300000:
        answer = price * 0.9
    elif price >= 100000:
        answer = price * 0.95
    else:
        answer = price
    
    return int(answer)

## 아이스 아메리카노 
def solution(money):
    max_coffee = money // 5500  # 최대로 마실 수 있는 아메리카노 잔 수
    remain_money = money % 5500  # 남는 돈
    
    return [max_coffee, remain_money]

# other solution
def solution(money):

    answer = [money // 5500, money % 5500]
    return answer

## 나이 출력
def solution(age):
    current_year = 2022

    birth_year = current_year - age + 1 # 선생님의 출생 연도 
    return birth_year

# other solution
from datetime import datetime

def solution(age):
    current_year = datetime.now().year # 현재 연도 
    birth_year = current_year - age + 1
    return birth_year

## 배열 뒤집기 
def solution(num_list):
    answer = num_list[::-1]
    return answer

# 리스트를 거꾸로 뒤집어 새로운 리스트로 반환하려면 reverse() 대신 슬라이싱을 사용하거나, reversed()를 활용 

# other solution
def solution(num_list):
    answer = list(reversed(num_list))
    return answer 