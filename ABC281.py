#A
# N  = int(input())
# list = []
# for i in range(N+1):
#     list.append(i)
# for s in reversed(list):
#     print(s)

#B
# S = input()
# if len(S) == 8:
#     if S[1:7].isdecimal() and int(S[1:7]) >= 100000:
#         if "A"<=S[0]<="Z":
#             if S[1:7].isdecimal() and 100000 <= int(S[1:7]) <= 999999:
#                 if "A"<=S[-1]<="Z":
#                     print("Yes")
#                 else:
#                     print("No")
#             else:
#                 print("No")
#         else:
#             print("No")
#     else:
#         print("No")
# else:
#     print("No")

#C
# N,T = map(int,input().split())
# A = list(map(int,input().split()))
# c = 0
# n = 0
# for i in A:
#     n += i
#     while c <= T:
#         c += i
#         n += i
# if c-T<=int(A[0]):
#     print(int(A[0])-(c-T))
            
