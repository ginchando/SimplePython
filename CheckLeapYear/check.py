year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
isLeapYear = False
if year % 400 == 0:
    isLeapYear = True
elif year % 4 == 0 and year % 100 != 0:
    isLeapYear = True
result = "is" if isLeapYear else "is not"
print(f"{year} {result} a leap year")

month_name = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
name = month_name.get(month)

month_days = {
    1: 31, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30,
    12: 31, 2: 29 if isLeapYear else 28
}
days = month_days.get(month)
print(f"{name} has {days} days")