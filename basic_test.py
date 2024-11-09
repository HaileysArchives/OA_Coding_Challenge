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