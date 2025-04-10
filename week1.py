# #집합 자료형 (set)
# #리스트랑 비슷한데 2가지 차이점이 존재
# #1. 중복을 허용하지 않음
# #2. 순서가 없음
# #리스트와 튜플은 순서가 있기 때문에 인덱싱 가능
# #딕셔너리와 셋은 순서가 없기 떄문에 인덱싱 불가능. 대신 특정 원소의 존재 여부 확인은 O(1)
# # 집합 자료형 초기화 방법 Set()함수를 이용하거나, 중괄호 안에 각원소를 콤마로 구분해서 넣어야함
#
# data = set([1,1,2,3,4,5,5])
# print(data)
#
# data = {1,1,2}
# print(data)
#
# a = set([1,2,3,4,5])
# b = set([3,4,5,6,7])
#
# print(a | b) #합집합
# print(a & b) #교집합
# print(a-b) #차집합
#
# data = set([1,2,3])
# print(data)
#
# #새로운 원소 추가
# data.add(4)
# print(data)
#
# #새로운 원소 추가 여러 개
# data.update([5,6])
# print(data)
#
# #특정한 값을 갖는 원소 삭제
# data.remove(3)
# print(data)

#추가 삭제 모두 시간복잡도 O(n)
#------------------------------------------------------------------------------------------------------------
# # 파이썬 조건문 if
# # 파이썬에서 조건문을 작성할 때는 if 키워드 사용
# # If 조건 : 실행할 코드
# # 코드의 블록을 들여쓰기로 설정 교재 "이왕이면 띄어쓰기 4번으로 할 수 있도록 습관을 들이는 것을 추천한다."
# # -> 파이썬 공식 스타일 가이드인 PEP 8에서 스페이스 4칸을 권장하는데, tab도 무관함
#
# # x in list : 리스트 안에 x가 들어 있을 때 참
# # x not in 문자열 : 문자열 안에 x가 들어 있지 않을 때 참
# # pass : 아무것도 처리하지 않음
# # 조건부 표현식(Conditional Expression) : if~else문을 한줄에 작성할때
# # 파이썬은 조건문 내 부등식을 수학과 같이 사용할 수 있음 -> if 0 < x < 20 (c의 경우 : if 0 < x and x < 20
#
# score = 85
#
# if score>=90:
#     print("학점 : A")
# elif score>=80:
#     print("학점 : B")
# elif score>=80:
#     print("학점 : C")
# else :
#     print("학점 : F")
#
# if score>=80:
#     pass # 나중에 작성할 소스코드
# else :
#     print("성적이 80점 미만")
#
# print("프로그램을 종료함")
#
# if score >= 80 : result = "Success"
# else : result = "Fail"
#
# result = "Success" if score >= 80 else "Fail"
# print(result)
#
# a = [1,2,3,4,5,5,5]
# remove_set = {3,5}
#
# result = []
# for i in a:
#     if i not in remove_set:
#         result.append(i)
#
# print(result)
#
# result2 = [i for i in a if i not in remove_set]
# print(result2)
#------------------------------------------------------------------------------------------------------------
# # 반복문
# i = 1
# result = 0
# # i가 9보다 작거나 같을 때 아래 코드를 반복적으로 수행
# while i <= 9:
#     result += i # result = result + i
#     i += 1
# print(result)
#
# result = 0
# # i는 1부터 9까지의 모든 값을 순회
# for i in range(1,10):
#     result += i
# print(result)
#
# score = [90,85,77,65,97]
# cheating_list = {2,4}
#
# for i in range(5):
#     if i+1 in cheating_list:
#         continue
#     if score[i] >= 80:
#         print(i+1, "번 학생은 합격")
#
# for i in range(2,10):
#     for j in range(1, 10):
#         print(i," x ", j)
#     print()
#------------------------------------------------------------------------------------------------------------
# # 함수
# # 사용자 정의 함수(user-defined function)
# # def함수명(매개변수): 실행할 소스코드, return 반환 값
#
# # 람다 표현식(Lambda Express): 한 줄식의 함수 정의를 통한 간단한 연산 및 로직 표현 -> Python 특징
# # 익명 함수 가능, 일회성 함수나 인자로 넘길 함수 만들 때 유용
#
# # 가독성 저하, 디버깅 어려울 수 있음
#
# def add(a=2,b=-1):
#     print("결과 : ", a+b)
#
# add(a=3)
#
# a=0
#
# def func():
#     global a
#     a += 1
#
# for i in range(10):
#     func()
# print(a)
#
# def add(a,b):
#     return a+b
#
# # 일반적인 add 매서드 사용
# print(add(3,1))
#
# # 람다 표현식
# print((lambda a,b: a+b)(3,2))
#------------------------------------------------------------------------------------------------------------
# # 입출력
# # n = input() -> 디폴트 자료형은 항상 문자열(str)
# # n = int(input()) -> 형변환을 통한 int 데이터로 입력 문자열 변환
# # 데이터를 공백으로 구분하여 입력 : n,m,k = map(int,input(),split())
# # 입력을 최대한 빠르게 받아야 할 때: import sys , sys.stdin.readline().rstrip()
# # rstrip() 함수는 readline()으로 입력에서의 엔터가 줄바꿈 기호로 인식되는데, 이 공백 문자를 제거하기 위해 사용함,
# # 관행적으로 외워서 사용
# #출력
# # print()로 처리
# # Python 3.6이상 f-string 문법 사용
# # print(f"정답은 {answer}이다")
#
# # # 데이터의 개수 입력
# # n = int(input())
# # # 각 데이터를 공백으로 구분하여 입력
# # data = list(map(int, input().split()))
# # data.sort(reverse=True)
# # print(data)
#
# # # n, m, k를 ','으로 구분하여 입력
# # n, m, k = map(int, input().split(","))
# # print(n,m,k)
# # print(type(n))
#
# # import sys
# # data = sys.stdin.readline().rstrip() # 관행 코드
# # print(data)
#
# # 출력할 변수들
# a=10
# b=2
# print("ddddddd"+str(a))
# print(f"dddd{a}")
#------------------------------------------------------------------------------------------------------------
#주요 라이브러리 유의점
# 표준라이브러리는 특정한 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리
# 주요 라이브러리 6가지
# 1. 내장 함수 : print(), input()
# 2. itertools : 반복 되는 형태의 데이터 처리 기능 제공
# 3. heapq : 힙(heap) 기능 제공, 우선순위 큐 기능을 구현하기 위해 사용
# 4. bisect : 이진 탐색 기능 제공, 사용 불가 존재
# 5. collections : 덱(deaue), 카운터(counter) 자료구조 포함
# 6. math : 수학적 기능 제공

# 내장 함수
# sum() 리스트와 같은 iterable 객체가 입력으로 주어졌을 때 모든 원소의 합을 반환
# min() 두 개 이상의 파라미터에서 가장 작은 값을 반환
# max() 두 개 이상의 파라미터에서 가장 큰 값을 반환
# eval() 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환
# sorted() iterable 객체에 대하여 정렬된 결과를 반환, Key 속성으로 정렬 기준 명시, reverse로 내림차순 가능
# 리스트와 같은 iterable 객체는 기본적으로 sort() 함수 내장

# 표준 라이브러리 - itertools
# permutations : 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 '순열'을 리턴
# combinations : 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 '조합'을 리턴
# product : 모든 순열을 리턴하되 원소를 중복으로 뽑는다. , 클래스이므로 객체 초기화 후 리스트 자료형으로 변환하여 사용 필요
# 표준 라이브러리 - math
# factorial() / sqrt() / gcd() : 최대 공약수를 리턴 / pi,e : 파이값과 자연상수 e를 리턴

result = sum([1,2,3,4,5])
print(result)
result = min(10,0,0.2)
print(result)
result = max(5,-22,5.6)
print(result)
result = eval("(3+5)*7")
print(result)
result = sorted([9,1,8,5,4],reverse=True)
print(result)
result = sorted([('길동',35),('이순신',75),('아무개',50)], key=lambda x:x[1])
print(result)
data = [9,1,2,555,0.1]
data.sort()
print(data)

import itertools
data = ['A', 'B', 'C'] # 데이터
result = list(itertools.permutations(data)) # 모든 순열
result2 = list(itertools.combinations(data,2)) # 조합
result3 = list(itertools.product(data,repeat=2)) # 2개를 뽑는 모든 순열 구하기, 중복 허용
result4 = list(itertools.combinations_with_replacement(data,2)) # 중복을 허용한 조합
print(result)
print(result2)
print(result3)
print(result4)

import math as m
print(m.factorial(5))
print(m.sqrt(9))
print(m.gcd(21,14))
print(m.pi, m.e)