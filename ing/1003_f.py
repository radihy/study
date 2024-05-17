
def fibo(_test_case):
    
    for _i in range(1, len(_test_case)):        
        _variable = int(_test_case[_i])
        # print(f'now variable is {_variable}')
        
        if _variable == 0:
            
            print('1 0')
            
        elif _variable == 1:
            
            print('0 1')
            
        else:
            _zero = 0
            _one = 0
            
            _num = _variable
            _first_term = _variable -1
            _second_term = _variable -2
            
            for _j in range(1, _variable):    
                print(f'f{_num} = f{_first_term} + f{_second_term}')                
                # if _second_term == 1:
                #    _one+=1
                #    _second_term = _first_term - 1
                   
                # elif _second_term ==0:
                #     _zero+=1
                #     _one+=1
                #     break
                    
                _first_term-=1
                _second_term-=1
                _num-=1
                
                 
    print(f'_zero is {_zero}')
    print(f'_one is {_one}')


        
if __name__  == '__main__' :
    test_case = open(0).readlines()
    test_case = [l.strip() for l in test_case]
    print(test_case)
    fibo(test_case)
    

# import time
# start = time.time()

# zero = 0
# one = 0

# def fibo(n):  
#     if n == 0:
#         zero+=1
#         return 0
#     elif n == 1:
#         one+=1
#         return 1
#     else:
#         first = n-1
#         for i in range(1, first):
#             if first == 0:
#                 zero+=1
#             elif first == 1:
#                 one+=1
#             else:
#                 first -=1
#         second = n-2
#         for i in range(1, second):
#             if second == 0:
#                 zero+=1
#             elif second == 1:
#                 one+=1
#             else:
#                 second-=1
#         # return first, second
#         # return fibo(n-1) + fibo(n-2)

# my_inputs=open(0).readlines()
    
# iterate_num = int(my_inputs[0])+1
# for i in range(1, iterate_num):
#     zero=0
#     one=0
#     fibo(int(my_inputs[i]))
#     print(f'{zero} {one}')

# end = time.time()
# print(f"{end - start:.5f} sec")