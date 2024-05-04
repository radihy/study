# 0. 입력받은 값을 list에 저장한다.
input_case = open(0).readlines()
input_case = [l.strip() for l in input_case]

print(input_case)


# 1. 밭을 만든다
iteration = int(input_case[0])
str_input = input_case[1]
field_x = int(str_input.split(' ')[0])
field_y = int(str_input.split(' ')[1])
field_n = int(str_input.split(' ')[2])

field = []
for i in range(field_y):
    line = []
    for j in range(field_x):
        line.append(0)
    field.append(line)

# field = [[0 for j in range(field_x)] for i in range(field_y)]

# 2. 배추 위치를 받아온다
cabbage = []
for i in range(2, 2+field_n): #대체
    cabbage.append(input_case[i])
    # cabbage = ['0 0', '1 0', '1 1', '4 2', '4 3', '4 5', '2 4', '3 4', '7 4', '8 4', '9 4', '7 5', '8 5', '9 5', '7 6', '8 6', '9 6']


for c in cabbage:
    x = int(c.split(' ')[0])
    y = int(c.split(' ')[1])
    # print(x, y)
    
    field[y][x] = 1


for x in field:
    print(x)

# print(type(field[0][1]))

if field[0][0] == 1:
    print("벌레")
    if field[-1][0] == 1: # 상
        print("벌레")
    if field[1][0] == 1: # 하     
        print("벌레")
    if field[-1][0] == 1: # 좌
        print("벌레")
    if field[1][0] == 1: # 우
        print("벌레")

