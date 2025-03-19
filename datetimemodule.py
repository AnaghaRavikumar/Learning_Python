import datetime

from Strings import message

gvr = datetime.date(1956, 1, 31)
print(gvr)

mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)
print(mill+dt) #positive number will increase the date, negative number  will decrease the date


#by default python displayed year month day, wee cna display the way we want
#Day-name, Month-name Day-#,  Year
print(gvr.strftime("%A, %B, %d, %Y"))

message = "GVR was born on {:%A, %B %D, %Y}."
print(message.format(gvr))

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27,0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)

print(launch_date)
print(launch_time)
print(launch_datetime)
print(launch_time.hour)
print(launch_time.minute)
print(launch_time.second)