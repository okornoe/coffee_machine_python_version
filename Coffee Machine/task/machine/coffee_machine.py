# Write your code here
UNIT_OF_WATER = 200
UNIT_OF_MILK = 50
UNIT_OF_COFFEE_BEANS = 15

print("Write how many cups of coffee you will need:")
num_cups_of_coffee = int(input())
print(f"For {num_cups_of_coffee} cups of coffee you will need:")

print(f"{UNIT_OF_WATER * num_cups_of_coffee} ml of water")
print(f"{UNIT_OF_MILK * num_cups_of_coffee} ml of milk")
print(f"{UNIT_OF_COFFEE_BEANS * num_cups_of_coffee} g of coffee beans")
