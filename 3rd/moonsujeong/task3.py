# #2675
# A = int(input()) #테스트 개수 입력(정수형)

# for i in range(A): 
#     B,C = input().split() #각 테스트에서 반복출력할 문자 개수와 문자 입력
#     for i in range(len(C)): 
#         print(int(B)*C[i], end='') #하나의 문자당 반복 출력 문자 개수 만큼 더해서 출력
#     print()

# #1152
# A = input().split()
# print(len(A))

# #1157
# W =input().lower() # 소문자 단어 입력
# WL = list(set(W)) #리스트로 묶어 모든 문자 나눔
# cnt=[]

# for i in WL:
#     c = W.count(i) # 특정 알파벳이 얼마나 반복됐는지 카운트
#     cnt.append(c) # 카운트 변수 리스트에 추가
# if cnt.count(max(cnt)) >=2: #반복되는 알파벳 두 개 이상
#     print("?") # ? 출력
# else:
#     print(WL[(cnt.index(max(cnt)))].upper()) #cnt 변수 리스트에 가장 큰 값의 대문자 알바벳 출력

# #1316
# N = int(input()) #테스트 개수 입력
# cnt = N

# for i in range(N):
#     w = input() #단어 개수 입력
#     for j in range(0, len(w)-1):
#         #그룹 단어가 아닐 경우
#         #중복 알파벳의 단어
#         if w[j] == w[j+1]: 
#         #카운트 x
#             pass
#         #같은 단어
#         elif w[j] in w[j+1:]:
#         #단어 카운팅 감소
#             cnt -= 1
#             break

# print(cnt)

# #25083
# print("         ,r\'\"7")
# print("r`-_   ,\'  ,/")
# print(" \\. \". L_r\'")
# print("   `~\\/")
# print("      |")
# print("      |")

# #3003
# n_list = [1, 1, 2, 2, 2, 8] #체스 구성
# y_list = list(map(int,input().split()))#발견한 흰색 피스 입력

# for i in range(6):
#     print(n_list[i] - y_list[i], end=' ') #흰색 피스 만큼 주어진 체스판에서 구성을 추가 및 제거 해야할 지 출력

# #2444
# n = int(input())#줄 별 최대 입력 별 개수 입력
# for i in range(1, n):
#     print(' '*(n-i) + '*'*(2*i-1)) #피라미드 정렬
# for i in range(n, 0, -1): #피라미드 정렬 역순
#     print(' '*(n-i) + '*'*(2*i-1))
    
# #10988
# w = list(str(input())) #문자열 리스트 입력

# if list(reversed(w)) == w: #역순 정렬 시 같은 단어 배열이면 
#     print(1) # 1 출력
# else: #같은 단어 배열이 아닐 경우 
#     print(0) #0 출력

# #2941
# c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# word = input() #단어 입력

# for i in c :
#     word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
# print(len(word))

# #25206
# rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
# grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

# total = 0	# 학점 총합을 담을 변수
# result = 0	# (학점 * 과목평점) 총합을 담을 변수
# for _ in range(20) :
#     s, p, g = input().split() #과목명, 학점, 등급
#     p = float(p)
#     if g != 'P' :	# 등급이 P인 과목은 계산 안함
#         total += p
#         result += p * grade[rating.index(g)] # 받은 점수 만큼 학점에 가중치 부여하여 결과에 저장

# print('%.6f' % (result / total))
