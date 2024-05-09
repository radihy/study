# for i in range(5):
#     print(i)
    
# i=0
# while i<5 :
#     print(i)
#     i+=1
#     print("hahaha")

# i=0
# while True:
#     i+=1
#     print(i-1)
#     if i==5:
#         break

# j=0
# while True:
#     i=0    
#     while True:
#         # 0~4 출력
#         print(i)
#         i+=1
#         if i == 5:
#             break
    
#     j+=1
#     if j == 2:         
#         break

# j=0
# while j<2:
#     i=0
#     while i<5:
#         print(i)
#         i+=1
#     j+=1
    
# 0 ~3 10번 출력

# j=0
# while j<10:
#     i=0
#     print(f"{j+1}번째 출력")
#     while i<4:
#         print(i)
#         i+=1
#     j+=1
    
   
# count = int(input("몇 번 반복할지 입력하세요 : "))
# j=0
# while j<count:
#     i=0
#     print(f"{j+1}번째 출력")
#     while i<4:
#         print(i)
#         i+=1
#     j+=1
    
# count = int(input("몇 번 반복할지 입력하세요 : "))

# 100,000 번에서 끊자
# 방법 1.
# k = 0
# for i in range(0, count):
#     print(f"{i+1}번째 반복")
#     for j in range(0, 4): # 0부터 3까지 j를 반복
#         print(j)
#     k+=1
#     if k == 100000:
#         break
        
# count = int(input("몇 번 반복할지 입력하세요 : "))
# 방법 2.
# for i in range(0, count):
#     if i == 100000:
#         break
#     print(f"{i+1}번째 반복")
#     for j in range(0, 4): # 0부터 3까지 j를 반복
#         print(j)


# i가 마지막 반복에서만 0과 1이 출력되게 해주세요
# count = int(input("몇 번 반복할지 입력하세요 : "))

# for i in range(0, count):
#     if i == 100000:
#         break
#     print(f"{i+1}번째 반복")
#     for j in range(0, 4): # 0부터 3까지 j를 반복
#         print(j)
#         if i == count-1:
#             print(j+1)
#             if j==0:
#                 break

# i가 마지막 반복에서만 0과 1이 출력되게 해주세요
# count = int(input("몇 번 반복할지 입력하세요 : "))

# for i in range(0, count):
#     if i == 100000:
#         break
#     print(f"{i+1}번째 반복")
#     for j in range(0, 4): # 0부터 3까지 j를 반복
#         if i == count-1:
#             print(j)
#             if j==1:
#                 break
#         else:
#             print(j)

            
# count = int(input("몇 번 반복할지 입력하세요 : "))

# for i in range(0, count):
#     if i == 100000:
#         break
#     print(f"{i+1}번째 반복")
#     for j in range(0, 4): # 0부터 3까지 j를 반복
#         print("j루프 실행")
#         print(j)
#         if i == count-1:
#             if j==1:
#                 break

# count = int(input("몇 번 반복할지 입력하세요 : "))

# for i in range(0, count):
#     if i == 100000:
#         break
#     print(f"{i+1}번째 반복")
#     for j in range(0, 4): # 0부터 3까지 j를 반복
#         print(j)
#         if (i == count-1) & (j == 1):
#                 break

count = int(input("몇 번 반복할지 입력하세요 : "))

for i in range(0, count):
    if i == 100000:
        break
    print(f"{i+1}번째 반복")
    for j in range(0, 4): # 0부터 3까지 j를 반복
        print(j)
        if ((i == count-1) or (i==99999)) & (j == 1):
            break

# 마지막 출력일 때 0 1만 출력해주세요
# 마지막 출력?
# i == count-1
# 