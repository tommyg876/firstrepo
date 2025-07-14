from time import time

now = time()
days = (now // 86400)

years = (int(days % 365 + 1970))

start = 12
duration = (now / 3600)
hour = (start + duration) % 12
minute = (hour - int(hour)) * 60
second = (minute - int(minute)) * 60


print (f"It has been {days} days since the epoch 1970")
print (f"The current time is {int(hour)}:{int(minute)}:{int(second)}")