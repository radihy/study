test_case = open(0).readlines()
test_case = [l.strip() for l in test_case]
# print(test_case)

for _i in range(0, int(test_case[0])):
    _iter_num = int(test_case[_i+1].split()[0])

    _iter_length = len(test_case[_i+1].split()[1])
    _str = ""
    for _j in range(0, _iter_length):
        _iter_str = test_case[_i+1].split()[1][_j]
        _str = _str+_iter_str*_iter_num
    print(_str)        