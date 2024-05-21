time = input().split()
hour = int(time[0])
minute = int(time[1])

# n시 45분 이상일 때
if minute >= 45:
    minute=minute-45
    print(hour, minute)
# n시 45분 미만일 때
else:
    minute=60+(minute-45)
    hour-=1
    # hour가 0시 이전일 때
    if hour < 0:
        hour=24+hour
    print(hour, minute)