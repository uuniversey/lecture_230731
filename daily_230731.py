

# 18046. 4828. min & max

# T = int(input())   #테스트 케이스 개수

# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))

#     ans = 0
#     max_v = arr[0]
#     min_v = arr[0]
#     for i in range(1, N):
#         if max_v < arr[i]:
#             max_v = arr[i]
#         if min_v > arr[i]:
#             min_v = arr[i]

#     ans = max_v - min_v

#     print(f'#{tc} {ans}')



# 1206. view

# T = 10

# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))

#     def tallest(my_list):

#         middle = my_list[2]

#         for idx, val in enumerate(my_list):
#             val -= middle
#             if val == 0 and idx != 2:
#                 return False
#             elif val > 0:
#                 return False   
                
#         return True

#     num = 0
#     for i in range(2, N-2):
#         my_list = [arr[i-2], arr[i-1], arr[i], arr[i+1], arr[i+2]]
            
#         if tallest(my_list) == True:
#             my_list2 = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]
#             max_v2 = 0
#             for j in my_list2:
#                 if j > max_v2:
#                     max_v2 = j
#                 else:
#                     continue
#             num += arr[i] - max_v2

        
#     print(f'#{tc} {num}')



# 4835. 구간합

# T = int(input())

# for tc in range(1, T+1):
#     N, M = map(int,input().split())
#     arr = list(map(int,input().split()))

#     box = []
#     for j in range(N-M+1):
#         num = 0
#         my_sum = 0
        
#         for i in range(M):
#             num = arr[j+i]
#             my_sum += num

#         box.append(my_sum)

#     my_max = 0
#     my_min = 10000000 

#     for k in box:
#         if k > my_max:
#             my_max = k    
#         if k < my_min:
#             my_min = k
        
#     result = my_max - my_min

#     print(f'#{tc} {result}')
    


        