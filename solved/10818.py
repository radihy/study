test_case = open(0).readlines()

test_case = list(map(int, test_case[1].split()))
print(f"{min(test_case)} {max(test_case)}")
