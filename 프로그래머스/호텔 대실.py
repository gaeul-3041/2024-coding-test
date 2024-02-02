def solution(book_time):
    schedule = []
    # 전체 시간대는 0초에서 24 * 60 + 10초까지 존재
    room = [0] * 1451

    # hh:mm을 초 단위 int로 변환
    for book in book_time:
        s, e = book
        int_s = int(s[0:2]) * 60 + int(s[3:])
        int_e = int(e[0:2]) * 60 + int(e[3:]) + 10
        schedule.append([int_s, int_e])

    # 누적합: 시작 시간에 +1, 종료 시간에 -1을 적용
    for time in schedule:
        s, e = time
        room[s] += 1
        room[e] -= 1
    
    for i in range(1, len(room)):
        room[i] += room[i-1]

    return max(room)
