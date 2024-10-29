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



