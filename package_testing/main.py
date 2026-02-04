# ============================== 1st way to import the module ===============================

# import my_calculator.addition
# import my_calculator.subtraction

# sum = my_calculator.addition.add(3, 4)
# difference = my_calculator.subtraction.sub(10, 6)

# print(f"Sum is {sum}")
# print(f"Difference is {difference}")

# ============================== 2nd way to import the module ===============================

# from my_calculator import addition, subtraction

# sum = addition.add(3, 4)
# difference = subtraction.sub(10, 6)

# print(f"Sum is {sum}")
# print(f"Difference is {difference}")

# ============================== 3rd way to import the module ===============================

# from my_calculator.addition import add
# from my_calculator.subtraction import sub

# sum = add(3, 4)
# difference = sub(10, 6)

# print(f"Sum is {sum}")
# print(f"Difference is {difference}")

# ============================== 4th way to import the module ===============================

from my_calculator import add, sub

sum = add(3, 4)
difference = sub(10, 6)

print(f"Sum is {sum}")
print(f"Difference is {difference}")
