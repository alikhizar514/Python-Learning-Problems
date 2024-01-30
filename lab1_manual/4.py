
class Time:
    def __init__(time_current_object, hours, min):
        time_current_object.hours = hours
        time_current_object.min = min
    def addTime(time_current_object, t1, t2):
        total_hours = t1.hours + t2.hours
        total_mins = t1.min + t2.min
        while((total_mins) >= 60):
            total_hours += 1
            total_mins -= 60
        time_current_object.hours = total_hours
        time_current_object.min = total_mins
    def displayTime(time_current_object):
        print("Time = ",time_current_object.hours,"h and ",time_current_object.min,"m.")

    def displayMinutes(time_current_object):
        hours = time_current_object.hours
        minutes = time_current_object.min
        while(hours>0):
            minutes += 60 
            hours -= 1
        print("Total Minutes : ",minutes)

t = Time(0,0)
t1 = Time(2,50)
t2 = Time(1,20)

t.addTime(t1,t2)
t.displayTime()
t.displayMinutes()
