for i in range(3):
    print(f"Inside the loop, i = {i}")

# Trying to access i outside the loop
try:
    print(f"Outside the loop, i = {i}")
except NameError:
    print("Error: 'i' is not defined outside the loop.")