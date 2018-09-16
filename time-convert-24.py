def time_converter(time):
    time_list = time.split(" ")
    
    if time_list[1] == 'p.m.' and  int(time_list[0].split(":")[0] + time_list[0].split(":")[1]) < 1200:
        int_time = int(time_list[0].split(":")[0])
        int_time += 12
        time_list[0] = str(int_time) + ":" +time_list[0].split(":")[1]
    
    if time_list[1] == 'a.m.' and  int(time_list[0].split(":")[0] + time_list[0].split(":")[1]) == 1200:
        time_list[0] = "00:00"

    if len(time_list[0].split(":")[0]) == 1:
        time_list[0] = '0' + time_list[0]
    
    return time_list[0]