num = int(input())
star = '*'
blank = ' '

for i in range(0, num):    
    num-=1    
    print(f'{blank*num}{star*(i+1)}')