#!/usr/bin/env python3
# ธนธรณ์
# รหัสนศ 670510755
# Sec001

def main():
    
    run_dist = \
    [4.1, 6.8, 4.5, 8.2, 6.5, 9.5, 7.2]
    run_time = \
    [16.4, 37.06, 33.75, 32.8, 39.0,
    71.25, 40.32]
    print(pace_record(run_dist, run_time))


    
def pace_record(run_dist, run_time):
    
    day = ['Sun', 'Mon',' Tue', 'Wed',' Thu', 'Fri' ,'Sat']
    day_re = list(reversed(day))
    time_ = list(map(lambda x,y: x / y ,run_time,run_dist))
    find_ = list(reversed(time_))
    min_ = min(time_)
    join = find_.index(min_)
    aws = time_ + [day_re[join]]
    
    return aws

if __name__ == '__main__':
    main()
    