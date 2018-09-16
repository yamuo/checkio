import calendar

def date_time(time: str) -> str:
    split_in = time.split(" ")
    print(split_in)
    date = split_in[0]
    time = split_in[1]
    ret = ""
    
    split_date = date.split(".")
    split_time = time.split(":")
    
    if split_date[0].startswith("0"):
        ret += split_date[0][1] + " "
    else :
        ret += split_date[0] + " "
    
    ret += calendar.month_name[int(split_date[1])] + " "
    
    ret += split_date[2] + " year "
    
    if split_time[0] == "01":
        ret += split_time[0][1] + " hour "
    elif split_time[0].startswith("0"):
        ret += split_time[0][1] + " hours "
    else :
        ret += split_time[0]  + " hours "
    
    if split_time[1] == "01":
        ret += split_time[1][1] + " minute"
    elif split_time[1].startswith("0"):
        ret += split_time[1][1] + " minutes"
    else :
        ret += split_time[1] + " minutes"

    return ret

print(date_time("01.01.2000 00:00"))


"""
if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""
