x=['순록','다람쥐','토끼','곰','거북이']
print(x.index('거북이')) # 지정한 데이터가 들어있는 자리를 숫자로 표현함 == 인덱스
# 인덱스는 선형 검색을 사용해 지정한 데이터를 찾는다
# 데이터가 여러개일 때는 가장 먼저 발견한 데이터의 인덱스를 반환함
# 데이터를 찾을 수 없을 땐 ValueError 발생


y=[['raccoon', 10, 300], ['fox', 40, 600], ['reindeer', 20, 500]]
# 배열 안에 배열이 들어있는 이중 구조

print([y for y in y if y[0]=='reindeer']) # 바깥쪽 칸의 맨 앞에서부터 차례로 살펴보고 안쪽 0번째 칸에 reindeer가 있는지 찾기
# 리스트 내포(comprehension) 기능 : [표현식 for 변수 in 반복가능한 대상]
# for y in y2 : 바깥쪽 칸 y2를 맨 앞부터 차례로 조사해 안쪽의 칸을 꺼내 y라고 이름붙임
# for y in y if y[0] == 'reindeer' : 안쪽 칸 y의 0번 데이터가 reindeer인지 조사
# 전체 : 만약 reindeer 찾으면 안쪽 칸 y를 결과 리스트로 처리

# 파이썬 특징 : 이로써 복잡한 처리 과정을 짧은 프로그램 언어로 작성가능

# 리스트 내포를 활용한 원소 단위 변환 (m->cm)
meter_list = [3, 7, 9, 10]
centi_meter_list = [100*i for i in meter_list]
# meter_list 요소를 for문을 돌며 각각 100*i 연산을 시켜 새로운 변수에 저장
print(centi_meter_list)

# 리스트 내포를 활용한 리스트 원소 제곱
meter_square_list = [i*i for i in meter_list]
print(meter_square_list)

# 리스트 내포를 활용한 원소 단위 변환 (m->cm) (홀수만)
centi_meter_list_odd = [100*i for i in meter_list if i%2 != 0]
print(centi_meter_list_odd)

# 리스트 내포를 활용한 이중 for문, 구구단 출력
result = []
for x in range(1, 10):
    # print(f'{x}단')
    for y in range(1, 10):
        result.append(x*y)
        # print(f'{x}단 x {y}는{x*y}')

# print(result)

result_list = [x*y for x in range(1, 10) for y in range(1, 10)] #구구단
result_list_even = [x*y for x in range(1, 10) if x%2 ==0 for y in range(1, 10)] # 짝수단만 출력
# print(result)
print(result_list_even)

