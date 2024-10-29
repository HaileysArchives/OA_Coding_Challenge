## 두 수의 합
def add(num1, num2):
    answer = num1 + num2
    return answer

## 두 수의 차
def minus(num1, num2):
    answer = num1 - num2
    return answer

## 두 수의 곱
def multi(num1, num2):
    answer = num1 * num2
    return answer

## 몫 구하기 
def quoti(num1, num2):
    answer = int(num1 / num2)
    return answer

## 두 수의 나눗셈
def div(num1, num2):
    answer = int((num1 / num2) * 1000)
    return answer

## 숫자 비교하기
def compare(num1, num2):
    if (num1 == num2):
        answer = 1
    else: 
        answer = -1
    
    return answer

## 분수의 덧셈
import math 

def add_fractions(numer1, denom1, numer2, denom2):
    lcm_denom = math.lcm(denom1, denom2) # least common multiple 최소공배수

    new_numer = numer1 * (lcm_denom // denom1) + numer2 * (lcm_denom // denom2) 

    gcd_value = math.gcd(new_numer, lcm_denom) # greatest common divisor 최대공약수

    return [new_numer // gcd_value, lcm_denom // gcd_value]

## 분수의 덧셈
import math 

def lcm(a, b):
    return a * b // math.gcd(a, b)

def add_fractions(numer1, denom1, numer2, denom2):
    lcm_denom = lcm(denom1, denom2)

    new_numer = numer1 * (lcm_denom // denom1) + numer2 * (lcm_denom // denom2)

    gcd_value = math.gcd(new_numer, lcm_denom)

    return [new_numer // gcd_value, lcm_denom // gcd_value]

## 배열 두 배 만들기 
def array_double(numbers):
    double_array = []

    for number in numbers:
        double_array.append(number * 2) 
    return double_array

def array_double(numbers):
    return [number * 2 for number in numbers] 

## 나머지 구하기 
def mod(num1, num2):
    answer = num1 % num2 
    return answer

cal_remainder = lambda num1, num2: num1 % num2

## 중앙값 구하기 
def median(array):
    array.sort()
    mid_index = len(array) // 2
    return array[mid_index]

## 최빈값 구하기 
def mode(array): 
    frequency = {} # 딕셔너리 구조 

    # 빈도 계산
    for num in array:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
        
    max_count = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_count]

    if len(modes) > 1:
        return -1
    else:
        return modes[0]

## 다른 풀이 
def mode(array):
    num = 0 # 최고 빈도 저장 
    data = 0 # 최빈값

    for i in set(array):
        if array.count(i) > num:
            num = array.count(i)
            data = i
        elif array.count(i) == num:
            data = -1
    return data 

## Counter(array): 배열의 각 요소 빈도를 계산하여 딕셔너리 형태로 저장 {1: 1, 2: 2, 3: 1}과 같은 결과를 얻음
from collections import Counter

def mode(array):
    counter = Counter(array)

    most_common = counter.most_common() # 빈도 순으로 정렬 
    max_count = most_common[0][1]

    modes = [num for num, count in most_common if count == max_count]

    if len(modes) > 1: # 최빈값이 여러 개인 경우
        return -1
    else:
        return modes[0]

## 짝수는 싫어요 
def odd(n):
    answer = []
    for i in range(1, n + 1):
        if (i % 2) != 0:
            answer.append(i)
    return answer