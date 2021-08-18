income = int(input())

if 23 <= income < 678:
    if (income // 23) > 1:
        print(f"{income // 23} chickens")
    else:
        print(f"{income // 23} chicken")

elif 678 <= income < 1296:
    if (income // 678) > 1:
        print(f"{income // 678} goats")
    else:
        print(f"{income // 678} goat")

elif 1296 <= income < 3848:
    if (income // 1296) > 1:
        print(f"{income // 1296} pigs")
    else:
        print(f"{income // 1296} pig")

elif 3848 <= income < 6769:
    if (income // 3848) > 1:
        print(f"{income // 3848} cows")
    else:
        print(f"{income // 3848} cow")

elif income >= 6769:
    print(f"{income // 6769} sheep")
else:
    print("None")
