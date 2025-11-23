print(" ---- Daily Step Counter ----")

days = int(input("How many days do you want to enter steps for? "))

total_steps = 0

for i in range(1, days + 1):
    steps = int(input("Enter steps for day " + str(i) + ":  "))
    total_steps = total_steps + steps

average = total_steps / days

print("\n Total steps in", days, "days:", total_steps)
print("average steps per day:", average)

if average < 3000:
    print("you activity level is low . try to walk more.")
elif average >= 3000 and average < 7000:
    print("your activity level is moderate.")
else:
    print("great! you are very active")