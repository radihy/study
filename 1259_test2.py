# 각 줄마다 주어진 수가 팰린드롬수면 yes, 아니면 no 출력
# [0]1 [1]2 [2]3 [3]4 [0]
# _iter가 어떤 범위에서, 어떤 변수로(_variable_length-1과 _iter가 같은 수이므로 선택의 여지 존재) 작동해야 가독성이 좋은지
# [_i]의 범위에서 반복문이 작동하는지, [_i][_n]의 범위에서 반복문을 작동시킬건지 헷갈렸다.
# break 위치, range 범위, range 사용유무, 범위 지정시 +1 할 것인지 등의 섬세한 부분에서의 실수 주의

def comparison (_test_case):
    _comparison_list = []

    for _j in range(1, len(_test_case)):
        _comparison_list.append([])
        for _k in range(0, len(_test_case[_j-1])):
            _comparison_list[_j-1].append(_test_case[_j-1][_k])

    return _comparison_list

    
def backwards(_comparison_list):
    for _i in range(0, len(_comparison_list)):

        _variable_length = int(len(_comparison_list[_i]))
        _iter = -1
        
        for _n in range(0, _variable_length//2): #_n이 0부터 (내부 리스트의 길이-1) 만큼 증가할 때
            if int(_comparison_list[_i][_n]) != int(_comparison_list[_i][_iter]):
                print("no")
                break
            _iter-=1       
        
        else:
            print("yes")
                
            

if __name__ == '__main__':
    # 입력을 받아옵니다.
    test_case = open(0).readlines()
    test_case = [l.strip() for l in test_case]
    
    # 입력을 이중 배열로 만들어줍니다.
    comparison_list = comparison(test_case)
    # 안쪽 배열에 대해 팰린드롬수인지 알아냅니다.
    backwards(comparison_list)
