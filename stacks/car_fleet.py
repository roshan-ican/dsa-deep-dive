position = [4, 1, 0, 7]
speed = [2, 2, 1, 1]
target = 10

by_pos = sorted(zip(position, speed), reverse=True)
print(by_pos, "___by_post__")
fleet = 0
fleet_time = 0

for p, s in by_pos:
    car_time = (target - p) / s
    if car_time > fleet_time:
        fleet+=1
        fleet_time = car_time
print(fleet)    
        
        
        