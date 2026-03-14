#Ask for hours worked and hourly
rate=float(input("How much company pays you hourly ? "))
daily_average_work_hour = float(input("Average daily working hour ? "))
hour_worked = daily_average_work_hour * 30
totoal_salary = hour_worked * rate
#   Print total salary.
print(f"You worked {hour_worked:.2f} hours monthly, and your salary is {totoal_salary:.2f}")
