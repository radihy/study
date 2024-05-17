def map_shape(_input_case):
    _size = _input_case[0].split()
    _size_x = int(_size[1])
    _size_y = int(_size[0])
    print(f'_size_x, _size_y is . . .{_size_x, _size_y}\n')

    # 맵 사이즈를 뺀 나머지(맵)만 남겨준다.
    _input_case.pop(0)
    print(f'the map is . . .{_input_case}\n')

    # 1차원 맵을 2차원 리스트로 변환한다.
    _chess_board = []
    for i in range(_size_y):
        print(i)
        _chess_board.append([_input_case[i]])

    print(f'_chess_board is . .. {_chess_board}\n')

    # 디버깅용 프린트
    print(_chess_board[0][0])
    print(type(_chess_board[0][0]))
    print(list(_chess_board[0][0]))
    print('\n')

    # 체스보드 내 타일 문자열을 문자로 변환해준다.
    _new_chess_board = []
    for i in range(_size_y):
        print(f'i is {i}')
        print(f'_chess board location is {_chess_board[i]}')
        print(list(_chess_board[i][0]))
        
        _new_chess_board.append(list(_chess_board[i][0]))
        
    print("\n최종 맵은 다음과 같다.")
    # print(_new_chess_board)
    print(*_new_chess_board, sep="\n")
    # print(_new_chess_board[0])
    return _new_chess_board, _size_y, _size_x


# 판 옮기기
def board_move(_new_chess_board, _size_y, _size_x):
    # 판을 한 커서씩 옮겨준다.
    for i in range(0, _size_x):
        for j in range(0, _size_y):
            # 한 커서를 오른쪽으로 이동했을 때 만약 n째줄의 길이가 8 미만이라면
            if len(_new_chess_board[i]) < 8:  # 맵 세로가 8 초과일때
            # 오른쪽으로는 그만 간다.
                pass
            else:
                _new_chess_board = _new_chess_board[0:8] # 맵을 8줄로 잘라준다
            
            # 한 커서를 아래로 내렸을 때 만약 지금 줄 ~ 마지막 줄 까지의 개수가 8 미만이라면
            if len(_new_chess_board) < 8:
            # 아래쪽으로는 그만 간다.
                pass
            else:
                for i in range(0, 8): # 8번 반복한다
                    _new_chess_board[i] = _new_chess_board[i][0:8] # i번째 줄의 가로길이를 8개로 잘라준다
                
            print("판 잘라주기 테스트")
            print(_new_chess_board)
        
    return _new_chess_board

# 판 잘라주기
def board_cut(_new_chess_board, _size_y, _size_x):
    
    if _size_y > 8: # 맵 세로가 8 초과일때
        _new_chess_board = _new_chess_board[0:8] # 맵을 8줄로 잘라준다
    else:
        pass
    
    if _size_x > 8: # 맵 가로가 8 초과일때
        for i in range(0, 8): # 8번 반복한다
            _new_chess_board[i] = _new_chess_board[i][0:8] # i번째 줄의 가로길이를 8개로 잘라준다
    else:
        pass
    
    print("판 잘라주기 테스트")
    print(_new_chess_board)
    



def answer():
    _white = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
    _black = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

    _answer_board1 = []
    _answer_board2 = []
    for i in range(4):
        _answer_board1.append(_white)
        _answer_board1.append(_black)
        _answer_board2.append(_black)
        _answer_board2.append(_white)

    print("\n첫번째 답안 판")
    print(*_answer_board1, sep="\n")
    print("\n두번째 답안 판")
    print(*_answer_board2, sep="\n")

    # print(len(new_chess_board))
    return _answer_board1, _answer_board2

def validation_board(_board_list, _answer_board1, _answer_board2):

    _wrong1=[]
    _wrong2=[]
    _count1 = 0
    _count2 = 0

    for j in range(0,len(_board_list)):
        for i in range(0, len(_board_list[j])):
            if _board_list[j][i] != _answer_board1[j][i]:
                # print("answer_board1에 없는 값은 : ")
                _wrong1.append(_board_list[j][i])
                _count1+=1
            if _board_list[j][i] != _answer_board2[j][i]:
                # print("answer_board2에 없는 값은 : ")
                _wrong2.append(_board_list[j][i])
                _count2+=1
    return _count1, _count2


if __name__ == '__main__':
    
    # 입력을 받아온다.
    input_case = open(0).readlines()
    input_case = [l.strip() for l in input_case]
    print(f'\ninput_case is . . . {input_case}\n')

    # 맵을 반환한다.
    new_chess_board, size_y, size_x = map_shape(input_case)

    # 판 옮기기
    new_chess_board = board_move(new_chess_board, size_y, size_x)
    
    # 8x8 체스보드의 정답판을 제작한다.
    # answer_board1, answer_board2 = answer()

    # # 맵과 정답판을 검증한다.
    # count_1, count_2 = validation_board(new_chess_board, answer_board1, answer_board2)

    # # 다시 칠해야 하는 정사각형 개수의 최솟값을 구해준다.
    # print("\n다시 칠해야 하는 정사각형 개수의 최솟값은")
    # if count_1>count_2:
    #     print(count_2)
    # else:
    #     print(count_1)


# 체스판의 [0][0]과 [0][1]을 비교하는 방식 싶패 -> 오류가 많음
# for i in range(size_y):
#     if len(new_chess_board) != 1:
#         print(i)
#         # print(f'new_chess_board[0][0] is . . . {new_chess_board[0][i]}')
#         print(f'new_chess_board[0] is . . . {new_chess_board[0]}')
#         if new_chess_board[0][0] == new_chess_board[0][1]:
#             count+=1
#             del new_chess_board[0][1]
#         else:
#             del new_chess_board[0][1]
#         print(f' del new_chess_board[0] is {new_chess_board[0]}')
#     else:
#         pass


# print(f'new_chess_board[0] is {new_chess_board[0]}')
# del new_chess_board[0][0]
# print(f'new_chess_board[0] is {new_chess_board[0]}')



# 원래 체스판과 비교하려 했는데 싶패 -> 오류가 많음
# test_case = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
# print(len(test_case))
# for i in range(len(test_case)):
#     for idx, val in enumerate(new_chess_board[i]):
#         print(f"val is . . . {val}")
#         print(f"idx is . . . {idx}")
#         print(f"test case i s . . . {test_case[i][idx]}")
#         if val == test_case[i][idx]:
#             pass
#         else:
#             count+=1