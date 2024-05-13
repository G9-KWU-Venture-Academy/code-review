# #25314
# for _ in range(int(input())//4): #4바이트 추가 저장 시 자료형에 long 하나 씩 더 붙임
#     print("long", end=" ")

# print("int") #마지막에 정수형 자료형 표현

#15552번
# import sys

# T=int(sys.stdin.readline()) #input 대신 sys.stdin.readline 활용 

# for i in range(0,T):
#     A,B=map(int,sys.stdin.readline().split()) #띄어쓰기로 숫자 구분 각각 변수에 저장
#     print(A+B)

#2439번
# import sys
# a=int(input()) #input -> sys.stdin.readline()
# for i in range(1,a+1):
#   print(" "*(a-i)+"*"*(i)) #줄바꿈 수 만큼 띄어쓰기후 * 출력

#10951번
# import sys
# while True:
#     try:
#         A, B = map(int, sys.stdin.readline().split())
#         print(A+B)
#     except:
#         break

#5597번
# students = [i for i in range(1,31)]

# for _ in range(28):
#     applied = int(input())
#     students.remove(applied) #1-30번 중 과제 제출 한 사람을 소거

# print(min(students)) #안낸사람 중 제일 앞 출석번호 출력
# print(max(students)) #다음 출석 번호 출력

#3052번
# arr = [] #리스트 생성
# for i in range(10):
#     a = int(input()) #입력(정수형)
#     if a%42 not in arr: #입력 값에서 42로 나눈 값이 리스트 내 에 없을 때
#         arr.append(a % 42) #리스트에 해당 값 추가
# print(len(arr)) # 리스트 출력

# #1546번
# subject = int(input()) #입력: 과목 개수
# scores = list(map(int, input().split()))# 입력: 각 과목 당 점수
# M = max(scores)#모든 과목 점수 중 최댓 값 뱐수에 저장

# for i in range(subject):
#     scores[i] = scores[i]/M*100 #문제에서 제시한 평균 계산 방법 적용

# print(sum(scores)/subject)
