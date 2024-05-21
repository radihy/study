# 입력을 받는다.
num = open(0).readlines()
num = [l.strip() for l in num]

# 나머지를 구한다.
for _i in range(0, 10):
    num[_i]=int(num[_i])%42
# print(num)

# 중복되는 값을 제거하면
num_set = list(set(num))
# print(num_set)

# count = {}
# for _j in num:
#     # 딕셔너리를 이용하여 숫자 _j가 있으면 값에 +1, 없으면 1로 값을 저장
#     try:
#         count[_j]+=1
#     except:
#         count[_j]=1

# # 딕셔너리의 키, 값 쌍을 가져와 값이 1인 키를 리스트로 저장
# new_num = []
# for _k, _v in count.items():
#     if _v >1:
#         new_num.append(_k)

# print(new_num)
print(len(num_set))