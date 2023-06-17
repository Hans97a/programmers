import math


def solution(fees, records):
    dic = {}
    for record in records:
        time, car_num, parking_type = record.split()
        h, m = map(int, time.split(":"))
        time = h * 60 + m

        if parking_type == "IN":
            try:
                dic[car_num]  # 이미 입차한 기록이 있는지 확인
                dic[car_num] = [
                    dic[car_num][0],
                    time,
                    False,
                    False,
                ]  # 해당 차의 누적주차시간, 입차시간, 첫번째 입차 여부, 정산 여부
            except:
                dic[car_num] = [0, time, True, False]
        else:
            in_time = dic[car_num][1]
            if dic[car_num][2] is True:  # 첫번째 출차라면
                dic[car_num][2] = False
                dic[car_num][0] = (time - in_time) - fees[0]
            else:
                dic[car_num][0] += time - in_time
            dic[car_num][3] = True

    result = []

    for car_num, arr in dic.items():
        total_parking, in_time, is_first, is_remitted = arr

        if not is_remitted:  # 입차만 했고 출차한 기록이 없는 경우 정산되지 않아 is_remitted 는 False
            out_time = 23 * 60 + 59
            dic[car_num][0] += out_time - in_time
            if is_first:
                dic[car_num][0] -= fees[0]
            total_parking = dic[car_num][0]

        if total_parking <= 0:
            fee = fees[1]
        else:
            fee = fees[1] + (math.ceil(total_parking / fees[2])) * fees[3]
        result.append([car_num, fee])

    result.sort(key=lambda x: x[0])

    return [car[1] for car in result]
