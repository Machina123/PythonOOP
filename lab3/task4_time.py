def gen_time(start, stop, hop):
    list_start = list(start)

    while True:
        yield tuple(list_start)
        tmpH = list_start[0] + hop[0]
        tmpM = list_start[1] + hop[1]
        tmpS = list_start[2] + hop[2]

        if tmpH > stop[0]:
            break
        else:
            if tmpH >= 24:
                list_start[0] = 0
            else:
                list_start[0] += hop[0]

            if tmpM > stop[1] and list_start[0] >= stop[0]:
                break;
            else:
                if tmpM >= 60:
                    list_start[0] += 1
                    list_start[1] = tmpM - 60
                else:
                    list_start[1] += hop[1]
                
            if tmpS > stop[2] and list_start[1] >= stop[1] and list_start[0] >= stop[0]:
                break
            else:
                if tmpS >= 60:
                    list_start[1] += 1
                    list_start[2] = tmpS - 60
                else:
                    list_start[2] += hop[2]

for time in gen_time((8,10,0), (10,50,15), (0,15,12)):
    print(time)