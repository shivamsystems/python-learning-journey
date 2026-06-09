dataset = ["100", "250", "ERR", "150", "N/A", "300"]
total_sum = 0
for data in dataset:
    try:
        value = int(data)
    except ValueError:
        print(f"Can't convert '{data}' to integer")
    else:
        total_sum += value

print(f"Expected output: {total_sum}")