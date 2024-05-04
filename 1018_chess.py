input_case = open(0).readlines()
input_case = [l.strip() for l in input_case]
print(input_case)
size = input_case[0].split()
size_x = int(size[0])
size_y = int(size[1])
print(size_x, size_y)

input_case.pop(0)
print(input_case)

chess_board = []
for i in range(size_y):
    chess_board.append([input_case[i]])

print(f'chess_board is . .. {chess_board}')
print(chess_board[0][0])
print(type(chess_board[0][0]))
print(list(chess_board[0][0]))

new_chess_board = []
for i in range(size_x):
    print(f'i is {i}')
    print(f'chess board location is {chess_board[i]}')
    print(list(chess_board[i][0]))
    
    new_chess_board.append(list(chess_board[i][0]))
    
print("맵 생성")
print(*new_chess_board, sep="\n")
print(new_chess_board[0][0])


count = 0

for i in range(size_y):
    if len(new_chess_board) != 1:
        print(i)
        # print(f'new_chess_board[0][0] is . . . {new_chess_board[0][i]}')
        print(f'new_chess_board[0] is . . . {new_chess_board[0]}')
        if new_chess_board[0][0] == new_chess_board[0][1]:
            count+=1
            del new_chess_board[0][1]
        else:
            del new_chess_board[0][1]
        print(f' del new_chess_board[0] is {new_chess_board[0]}')
    else:
        pass

wwbwbw
wbwbw
wwbw



# print(f'new_chess_board[0] is {new_chess_board[0]}')
# del new_chess_board[0][0]
# print(f'new_chess_board[0] is {new_chess_board[0]}')