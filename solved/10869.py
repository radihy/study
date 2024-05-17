test_case = open(0).readlines()
test_case = [l.strip() for l in test_case][0].split()


def add(_num_1, _num_2) :
    print(_num_1 + _num_2)
    
def subtract(_num_1, _num_2) :
    print(_num_1 - _num_2)
    
def multiply(_num_1, _num_2) :
    print(_num_1 * _num_2)
    
def quotient(_num_1, _num_2) :
    print(_num_1 //_num_2)
    
def remainder(_num_1, _num_2) :
    print(_num_1 % _num_2)

num_1 = int(test_case[0])
num_2 = int(test_case[1])

add(num_1, num_2)
subtract(num_1, num_2)
multiply(num_1, num_2)
quotient(num_1, num_2)
remainder(num_1, num_2)