import random
power655 = []
while len(power655) < 6:
    lucky_number = random.randint(1, 55)
    if lucky_number in power655:
        continue
    power655.append(lucky_number)
print("Your ticket number is: ", sorted(power655))