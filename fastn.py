import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
hr = int(time.strftime("%H"))
print(hr, "Hour right now in 24 hour notation ")
mi = int(time.strftime("%M"))
print(mi, "Minute right now ")
se = int(time.strftime("%S"))
print(se, "Second right now ")

#------------------------------------------------------------------------------------------
if hr <= 11 :
    print("Good Morning")
elif hr >= 20 :
    print("Good Night")
elif hr >= 17 :
    print("Good Evening")
else :
    print("Good Afternoon")
