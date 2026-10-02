principal = float(input("Enter principal: "))
rate = float(input("Enter rate (%): "))
time = float(input("Enter time (years): "))

si = (principal * rate * time) / 100
print(f"Simple Interest = {si}")
print(f"Total amount = {principal + si}")