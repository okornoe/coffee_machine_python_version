unit = int(input())

if unit < 1:
    print("no army")
elif 1 <= unit <= 9:
    print("few")
elif 10 <= unit <= 49:
    print("pack")
elif 50 <= unit <= 499:
    print("horde")
elif 500 <= unit <= 999:
    print("swarm")
elif unit >= 1000:
    print("legion")
