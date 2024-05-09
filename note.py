# 파이썬은 아래로, 탭
br = False
for i in range(5): # i가 0부터 4까지 반복 
    for j in range(10): # j가 0부터 9까지 반복
        print(0)
        if i==1: #i가 1이면
            br = True #br은 True
            break # 두 번째 반복문 종료
    if br: # br이 true면
        break # 첫 번째 반복문 종료

        
_new_chess_board = [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
['B', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'B'],
['B', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'B'],
['B', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'B'],
['B', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'B'],
['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]

_size_x = 13 # 13개의 요소
_size_y = 10 # 10개의 줄
for i in range(_size_y): # i가 0~9만큼 반복
    if len(_new_chess_board) < 8: # 전체 줄이 8줄 미만일때
        break # i 변수 있는 반복문 끝남
    else: # 전체 줄이 8 이상일때
        _new_chess_board = _new_chess_board[0:8] # 전체 줄을 8개로 잘라준다
        
    for j in range(_size_x): #j가 0~12만큼 반복
        print(f"j는 {j}번째") 
        print(f"i는 {i}번째") 
        if len(_new_chess_board) < 8: # 전체 줄이 8줄 미만일때
            break # j 변수 있는 반복문 끝남
        
        if len(_new_chess_board[i]) < 8: # i번째 줄 요소 개수가 8 미만일때
            break # j 변수 있는 반복문 끝남
        else: # i번째 줄 요소 개수가 8 이상일때
            for k in range(0, 8): # 0에서 7만큼 k가 반복한다
                _new_chess_board[k] = _new_chess_board[k][0:8] # k번째 줄의 요소를 8개로 잘라준다
            print("판 잘라주기 테스트")
            print(_new_chess_board)
    break
print('x')
