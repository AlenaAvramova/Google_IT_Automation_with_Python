import os 
os.system("cls")

#How many seconds are in 42 minutes 42 seconds?
print("\n\tTask1 ")  

minutes = 42.42
total_seconds = minutes * 60 + 42

print("seconds =", total_seconds)

#How many miles are there in 10 kilometers if 1 mile = 1.61 km?
print("\n\tTask2 ")

km = 10
mile_in_km =1.61
total_miles = km/mile_in_km

print("10 km in miles is: ", round(total_miles,2))

#If you run 10 km in 42 minutes 42 seconds,
#what is your average pace (time per mile)?
print("\n\tTask3 ")

average_pace = total_seconds/total_miles

print("The average pace is: ", round(average_pace, 2))