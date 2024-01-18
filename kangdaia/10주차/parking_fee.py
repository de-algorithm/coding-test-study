def calculate_fee(fees: list[int], records: list[str]) -> list[int]:
    base_time, base_fee, unit_time, unit_fee = fees
    record_dict = dict()
    car_time_cal = dict()
    result = []
    for record in records:
        time, car_id, record_type = record.split()
        hour, minute = time.split(":")
        if record_type == "IN":
            record_dict[car_id] = [(int(hour), int(minute))]
            pass
        else:
            in_time = record_dict[car_id].pop()
            total_time = (int(hour) - in_time[0]) * 60 + (int(minute) - in_time[1])
            car_time_cal[car_id] = car_time_cal.get(car_id, 0) + total_time
    
    for car_id, timestamp in record_dict.items():
        if len(timestamp) > 0:
            in_time = timestamp.pop()
            total_time = (23 - in_time[0]) * 60 + (59 - in_time[1])
            car_time_cal[car_id] = car_time_cal.get(car_id, 0) + total_time
    
    for _, total_minutes in sorted(car_time_cal.items()):
        over_time_fee = 0
        if total_minutes > base_time:
            over_time = total_minutes-base_time
            over_time_fee = (int(over_time/unit_time) + (over_time%unit_time>0)) * unit_fee
        result.append(base_fee+over_time_fee)
    return result