# # 거스름돈 문제
# # Q : N의 개수만큼 각기 다른 동전 값을 입력받을 때, 무한히 존재한다고 가정할때, 거스름돈 N에 대하여 최소한의 동전 개수를 구하라. N은 10의 배수이다.
# from boltons.iterutils import first
#
# n = 5000
# count = 0
# # 큰 값의 화폐부터 차례대로 확인
# coin_type = [500,100,50,10]
#
# for coin in coin_type:
#     count += n//coin
#     n = n % coin
#
# print(count)


# # 큰 수의 법칙
# # 크기가 N인 배열이 주어짐, 주어진 수들을 M번 더하여 가장 큰 수를 만듬, 단 배열의 특정 수는 연속해서 최대 K번까지 더해질 수 있음
# # N,M,K 입력
# n, m, k = map(int, input().split())
# # N개의 수를 공백으로 구분하여 입력 받기
# data = list(map(int,input().split()))
#
# data.sort() # 입력받은 수를 정렬
# first = data[n-1] # 가장 큰 수
# second = data[n-2] # 두번째로 큰 수
#
# # 첫 번째 답안
# result = 0
# while True:
#     for i in range(k): # 가장 큰 수를 k번 더하기
#         if m==0: #m이 0이면 반복문 탈출
#             break
#         result += first
#         m-=1
#     if m==0: # m이 0이라면 반복문 탈출
#         break
#     result += second # 두번째로 큰 수는 한번만 더하기
#     m -= 1 # 더할때마다 1씩 빼기
# print(result)
#
# # 두번 째 답안
# count = int(m/(k+1)) * k
# count += m%(k+1)
# result = 0
# result += (count)*first
# result += (m-count)*second # 두번째로 큰 수 더하기
# print(result)


# 숫자 카드 게임
# n x m 형태로 놓인 데이터를 받음
# 뽑고자 하는 행을 선택하는데 이때 선택한 행에서 가장 작은 숫자가 내가 택한 숫자가됨
# 가장 큰 수를 뽑을 수 있는 행을 선택해야 함
# 첫 번째 풀이 방법
# n,m 받기
# n, m = map(int, input().split())
# result = 0
# #한줄씩 입력받아 확인
# for i in range(n):
#     data = list(map(int, input().split()))
#     # 현재 줄에서 가장 작은 수 찾기
#     min_value = min(data)
#     # '가장 작은 수' 들 중에서 가장 큰 수 찾기
#     result = max(result, min_value)
# print(result)
# 두 번째 풀이 방법
# n, m = map(int, input().split())
# result = 0
# for i in range(n):
#     data = list(map(int, input().split()))
#     #현재 줄에서 가장 작은 수 찾기
#     min_value = 10001
#     for a in data:
#         min_value = min(min_value,a)
#     #가장 작은 수들 중에서 가장 큰 수 찾기
#     result = max(result, min_value)
#
# print(result)


# 실전문제 : 1이 될 때까지
# 입력받은 수 n이 1이 될때까지 두 과정 중 하나를 반복함
# 1. n에서 1을 뺀다 / 2. n을 k로 나눈다. (단 k로 나눌 수 있을 때만 가능)
# 가능한 최소 수행 횟수를 구하라.
# n, k = map(int, input().split())
# result = 0
# # n이 k이상이라면 k로 계속 나누기
# while n>=k:
#     # n이 k로 나누어떨어지지 않는다면 n에서 1씩 빼기
#     while n%k != 0:
#         n -= 1
#         result += 1
#     # k로 나누기
#     n//=k
#     result += 1
# #마지막으로 남은 수에 대하여 1씩 빼기
# while n>1:
#     n -= 1
#     result += 1
# print(result)


# 기출문제 '곱하기 혹은 더하기'
# 문자열 s가 주어졌을 때, x또는+ 연산자를 ㅓㄶ어 결과적으로 만들 수 있는 가장 큰 수를 구하는 프로그램을 작성
# 각 자리는 0부터 9, 모든 연산은 무조건 왼쪽부터 이루어짐
# data = input()
# # 첫번째 문자를 숫자로 변경하여 대입
# result = int(data[0])
# for i in range(1,len(data)):
#     # 두 수 중에서 하나라도 0 또는 1인 경우 더한다.
#     num = int(data[i])
#     if num <=1 or result <=1:
#         result+=num
#     else:
#         result*=num
# print(result)


# 만들 수 없는 금액
# n 개의 동전을 갖고 있으며, 만들 수 없는 최소 금액을 만들어라
# n = int(input())
# data = list(map(int, input().split()))
# data.sort() # 오름차순
# target = 1
# for x in data:
#     # 만들 수 없는 금액을 찾을 때 반복 종료
#     if target<x:
#         break
#     target += x
# # 만들 수 없는 금액 결과
# print(target)


# 회의실 배정 문제
# n개의 회의 와 각각의 회의는 시작시간 s와 끝나는 시간 e가 주어짐
# 할 수 있는 최대의 회의 개수를 찾아야함
# def max_meeting(meeting):
#     global meetings
#     # 회의의 종료 시간을 기준으로 오름차순 정렬
#     meetings.sort(key=lambda meeting:meeting[1])
#     count = 0 # 선택한 회의 수
#     last_end_time = 0 # 마지막 선택된 회의 종료 시간
#     # 정렬된 회의 목록에서 회의를 선택한다
#     for start,end in meetings:
#         # 현재 회의의 시작 시간이 이전에 선택된 회의의 종료시간보다 크거나 같으으면
#         if start >= last_end_time:
#             count += 1 # 회의를 카운트에 추가
#             last_end_time = end # 마지막 종료시간을 갱신
#     return count
#
# n = int(input("회의 개수를 입력하시오"))
# meetings = []
# for _ in range(n):
#     # 각 회의 시간의 시작과 끝을 입력받음
#     start, end = map(int, input().split())
#     meetings.append([start, end])
#
# #user_defined function 연습
# result = max_meeting(meetings)
# print(result)


# import requests
# target = "https://google.com"
# response = requests.get(url=target)
# print(response.text)


import requests
# REST API 경로에 접속하여 응답 데이터 받아오기
target = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url=target)
# 응답 데이터가 JSON 형식이므로 파이썬 객체로 변환
data = response.json()
# 모든 사용자(user) 정보를 확인하여 이름 정보만 삽입
name_list = []
for user in data:
    name_list.append(user["name"])
print(name_list)





















