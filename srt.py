from SRT import SRT
from time import sleep
import os
srt = SRT("010-****-****", "PW")

dep = '수서'
arr = '대전'
date = '20220912'
time = '110000'
book = 0
book_limit = 3
dep_limit = 17

while book <= book_limit:
    try:
        print("search...")
        trains = srt.search_train(dep, arr, date, time)

        for train in trains:
            print(train)
            if int(str(train).split('~')[1].split('(')[1].split(':')[0]) < dep_limit:
                reservation = srt.reserve(train)
                print("=== REV : ", end='')
                print(reservation)
                os.system( "say SRT reservation"  )
                book += 1
        sleep(1)
    except Exception as e:
        print(e)
        continue
