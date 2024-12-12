## 배열 자르기 
def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1] # slicing
    return answer

## 외계행성의 나이 
def solution(age):
    result = ""
    
    for digit in str(age):
        result += chr(97 + int(digit))
    
    return result

# other solution
def solution(age):
    answer = ''
    alpha = ['a' ,'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    age = str(alpha)
    
    for i in age:
        answer += alpha[int(i)]

    return answer

## 진료순서 정하기 
def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)

    # dictionary type
    answer = {}
    for index, value in enumerate(sorted_emergency):
        answer[value] = index + 1
    
    result = []
    for value in emergency:
        result.append(answer[value])
    
    return result

# enumerate(): 반복문에서 순회할 때 각 요소롸 함께 인덱스 제공

# .sorted(list): 새로운 정렬된 리스트를 반환
# list.sort(reverse=True): 원본 리스트를 직접 정렬 (reverse=True: 내림차순) 
# sort_values(): DataFrame 또는 Series 객체에서 사용하는 메서드

# other solution
def solution(emergency):
    answer = []
    sort_num = sorted(emergency, reverse=True)

    for i in emergency:
        answer.append(sort_num.index(i) + 1)

    return answer

## 순서쌍의 개수 
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if (n % i) == 0:
            answer += 1
    return answer

## 개미 군단
def solution(hp):
    ba = 5
    ma = 3
    sa = 1

    ba_answer = hp // ba 
    ma_answer = (hp - (ba_answer * ba)) // ma
    sa_answer = (hp - ((ba_answer * ba) + (ma_answer * ma))) // sa

    answer = ba_answer + ma_answer + sa_answer 
    return answer

# another solution
def solution(hp):
    ba = 5
    ma = 3
    sa = 1

    ba_answer = hp // ba
    hp %= ba

    ma_answer = hp // ma
    hp %= ma

    sa_answer = hp // sa

    answer = ba_answer + ma_answer + sa_answer
    return answer 

# another solution 
def solution(hp):
    answer = hp // 5 + ((hp % 5) // 3) + ((hp % 5) % 3)
    return answer 

## 모스부호(1)
def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    } # dictionary type 

    morse_list = letter.split(" ")

    answer = ""
    for alpha in morse_list:
        answer += morse[alpha]
    return answer 

## 가위바위보
def solution(rsp):
    rock = 0
    scissor = 2 
    paper = 5

    win_dict = {scissor:'0', paper:'2', rock:'5'}

    # for char in rsp:
    #     win = win_dict[char]

    answer = "".join([win_dict[char] for char in rsp])
    return answer 

# another solution 
def solution(rsp):
    win_dict = {
        '2': '0', 
        '0': '5',  
        '5': '2'  
    } 

    result = "".join([win_dict[char] for char in rsp])
    
    return result

## 구슬을 나누는 경우의 수 

## 점의 위치 구하기 

## 2차원으로 만들기 

## 공 던지기 

## 배열 회전시키기 
