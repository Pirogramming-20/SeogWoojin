class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    @staticmethod
    def is_time_valid(time_string):
        time=list(map(int,time_string.split(':')))
        if time[0]<=24 and time[1]<60 and time[2]<=60:
            return True
        else:
            return False
        
    @classmethod
    def from_string(cls,time_string):
        time=list(map(int,time_string.split(':')))
        t=cls(time[0],time[1],time[2])
        return t

time_string = input()
 
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')