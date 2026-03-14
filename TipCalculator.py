#exercise - tip calculator
bill_ammount = float(input("Bill ammount: "))
service_quality =input("Service Quality (good/fair/bad): ")

if service_quality == "good":
    tip = bill_ammount * (20/100)
    total = tip + bill_ammount
    print(f"Your tip is {tip} and final ammount is {total}")

elif service_quality == "fair":
    tip = bill_ammount * (15/100)
    total = tip + bill_ammount
    print(f"Your tip is {tip} and final ammount is {total}")
    
elif service_quality == "bad":
    tip = bill_ammount * (10/100)
    total = tip + bill_ammount
    print(f"Your tip is {tip} and final ammount is {total}")

