def sun_angle(time):
    l = time.split(':')
    l[0] = int(l[0])
    l[1] = int(l[1])
    h = 180/12
    m = 180/720
    angle = round(float((l[0]-6)*h + l[1]*m),2)

    if angle < 0 or angle > 180:
        return "I don't see the sun!"
    else:
        return angle



print(sun_angle("15:35"))
