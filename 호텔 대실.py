def solution(book_time):
    rooms = []

    to_minute = []
    for start, end in book_time:
        enter_h, enter_m = map(int, start.split(":"))
        end_h, end_m = map(int, end.split(":"))

        to_minute.append([enter_h * 60 + enter_m, end_h * 60 + end_m + 10])
    to_minute.sort(key=lambda x: x[0])
    print(to_minute)
    for room_enter, room_exit in to_minute:
        if not rooms:
            rooms.append([room_enter, room_exit])
        else:
            check = False
            for idx, room in enumerate(rooms):
                if room[1] <= room_enter:
                    rooms[idx] = [room_enter, room_exit]
                    check = True
                    break
            if check is False:
                rooms.append([room_enter, room_exit])

    return len(rooms)
