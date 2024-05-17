import time

if __name__ == "__main__":
    start = time.time()
    input_list = open(0).readlines()

    t = int(input_list.pop(0))
    for _ in range(t):
        n = int(input_list.pop(0))

        if n==0:
            print("1 0")
            continue
        elif n==1:
            print("0 1")
            continue

        counts = [[0, 0] for _ in range(n+1)] # [[0,0], [0,0], [0,0], [0,0]]
        counts[0][0] = 1 # [[1,0], [0,0], [0,0], [0,0]]
        counts[1][1] = 1 # [[1,0], [0,1], [0,0], [0,0]

        for i in range(2, n+1): # i == 2일때
            bef1 = counts[i-1] # counts[1] == [0,1]
            bef2 = counts[i-2] # counts[0] == [1,0]
            counts[i] = [bef1[0]+bef2[0], bef1[1]+bef2[1]] # [0+1, 1+0] == [1,1] == counts[2]
        
        print(*counts[n], sep=" ")
    end = time.time()
    print(f'{end-start:.5f} sec')