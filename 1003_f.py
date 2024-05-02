import time
start = time.time()

zero = 0
one = 0

def fibo(n):
    global zero, one
    if n == 0:
        zero+=1
        return 0
    elif n == 1:
        one+=1
        return 1
    else:
        first = n-1
        for i in range(1, first):
            if first == 0:
                zero+=1
            elif first == 1:
                one+=1
            else:
                first -=1
        second = n-2
        for i in range(1, second):
            if second == 0:
                zero+=1
            elif second == 1:
                one+=1
            else:
                second-=1
        # return first, second
        # return fibo(n-1) + fibo(n-2)

my_inputs=open(0).readlines()
    
iterate_num = int(my_inputs[0])+1
for i in range(1, iterate_num):
    zero=0
    one=0
    fibo(int(my_inputs[i]))
    print(f'{zero} {one}')

end = time.time()
print(f"{end - start:.5f} sec")