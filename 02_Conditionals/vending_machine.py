print("Water bottle cost 50 cents")
print("Ammount Due: 50 cents")
final = 50
while final >= 0:
    coin = int(input("Please insert the coin (5/10/15): "))
    if coin == 5 or coin == 10 or coin == 15:
        final = final - coin
        print(f"Ammount Due: {final} cents")
    else:
        print("Please insert valid coin")
        