# 입력을 리스트로 받아오기
input_num = []
for i in range(3):
    input_num.append(int(input()))


# 입력을 서로 곱해주기
output = list(str(input_num[0] * input_num[1] * input_num[2]))

# 숫자를 세기위한 딕셔너리 생성
num={}
for i in range(0, 10):
    num[i]=0


# 곱한 수에서 각 자리 수가 몇 번씩 쓰였는지 체크
for i in output:
    for j in num:        
        if int(i) == j:
            num[j] += 1
            

# 딕셔너리 출력
for i in num:
    print(num[i])