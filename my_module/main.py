# ============================== 1st way to import the module ===============================

# import addition 

# result = addition.add(5, 6)
# print(f"Result in {result}")


# ============================== 2nd way to import the module ===============================

# import addition as ad

# result = ad.add(5, 6)
# print(f"Result in {result}")

# ============================== 3rd way to import the module ===============================

# from addition import * # this is not good programing practice


# ============================== 4th way to import the module (import the mudule funtion)===============================

from addition import mul , add

result = mul(5, 6)
print(f"Result in {result}")

result = add(5, 6)
print(f"Result in {result}")




