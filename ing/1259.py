# 각 줄마다 주어진 수가 팰린드롬수면 yes, 아니면 no 출력
# [0]1 [1]2 [2]3 [3]4 [0]

def comparison (_test_case):
    _comparison_list = []

    for _j in range(1, len(_test_case)):
        # print(_test_case[_j-1])
        _comparison_list.append([])
        for _k in range(0, len(_test_case[_j-1])):
            # print(_test_case[_j-1][_k])
            _comparison_list[_j-1].append(_test_case[_j-1][_k])

    # print(_comparison_list)
    return _comparison_list

    
def backwards(_comparison_list):
    for _i in range(0, len(_comparison_list)):

        _variable_length = int(len(_comparison_list[_i]))
        _iter = -1
        
        # 내부 배열 안 인덱스 개수가 짝수이면
        if _variable_length%2 == 0:
            # print(f"_variable_length는 {_variable_length}")            
            
            for _n in range(0, _variable_length): #_n이 0부터 (내부 리스트의 길이-1) 만큼 증가할 때
                # print((_variable_length//2)-1)
                
                if int(_comparison_list[_i][_n]) == int(_comparison_list[_i][_iter]):
                    # print(int(_comparison_list[_i][_n]))
                    # print(int(_comparison_list[_i][_iter]))
                    _iter-=1
                    if _n == ((_variable_length//2)-1):
                        if _comparison_list[_i][_n] == _comparison_list[_i][_n+1]:
                            print("yes")
                            break
                        else:
                            print("no")
                            break
                else:
                    print("no")
                    break

        # 홀수이면
        else:
            # print(f"{_i}는 홀수")
            for _n in range(0, _variable_length): #_n이 0부터 (내부 리스트의 길이-1) 만큼 증가할 때
                # print((_variable_length//2)-1)
                
                if int(_comparison_list[_i][_n]) == int(_comparison_list[_i][_iter]):
                    # print(int(_comparison_list[_i][_n]))
                    # print(int(_comparison_list[_i][_iter]))
                    _iter-=1
                    if _n == (_variable_length//2):                        
                        print("yes")
                        break              
                else:
                    print("no")
                    break
            

if __name__ == '__main__':
    # 입력을 받아옵니다.
    test_case = open(0).readlines()
    test_case = [l.strip() for l in test_case]
    # print(test_case[:-1])
    
    # 입력을 이중 배열로 만들어줍니다.
    comparison_list = comparison(test_case)
    # 안쪽 배열에 대해 팰린드롬수인지 알아냅니다.
    backwards(comparison_list)
