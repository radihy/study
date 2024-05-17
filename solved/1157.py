# 입력을 받아 모두 소문자로 전환
string = input().lower() 
# 문자열 내 문자 하나하나를 리스트에 넣어줌
string = list(string)
real_string = string
# 리스트 내 중복 제거
string = list(set(string)) 

# 알파벳 저장 리스트
alphabet = {
    'a':0,
    'b':0,
    'c':0,
    'd':0,
    'e':0,
    'f':0,
    'g':0,
    'h':0,
    'i':0,
    'j':0,
    'k':0,
    'l':0,
    'm':0,
    'n':0,
    'o':0,
    'p':0,
    'q':0,
    'r':0,
    's':0,
    't':0,
    'u':0,
    'v':0,
    'w':0,
    'x':0,
    'y':0,
    'z':0
}

def slice(string, real_string, alphabet):
    # 가장 많이 출력된 알파벳과 그 빈도수를 저장
    max_var = 1
    max_str = "none"  

    # 중복이 제거된 리스트에서(쓰인 알파벳 종류를 알 수 있음)
    for i in string: # h e l o
        now_var = 0
        
        # 원래의 리스트에서(쓰인 알파벳의 개수까지 알 수 있음)
        for k in real_string: # h e l l o
            # 중복 제거된 리스트가 가리키는 알파벳과 원래의 리스트가 가리키는 알파벳이 같다면 +1 (알파벳 개수 세기)
            if k == i:
                now_var+=1
                alphabet[k] = now_var
    
    # 알파벳의 빈도수 값을 리스트로 반환
    list_var = list(alphabet.values())
    # 해당 리스트의 최대값 저장
    max_var = max(list_var)
    count = 0

    # 가장 높은 빈도수를 가진 알파벳 대문자로 저장
    for j in alphabet:
        if alphabet[j] == max_var:         
            max_str = j.upper()
            count+=1

    # 가장 높은 빈도수를 가진 알파벳의 중복 체크, 그렇지 않으면 가장 높은 빈도수를 가진 알파벳 출력
    if count >= 2:
        print("?")
    else:        
        print(max_str)

slice(string, real_string, alphabet)
