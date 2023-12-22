a = input()
b = a.split()

# Check if "तिरछे टाइप हमारे" is in the list and remove it
if "तिरछे" in b and "टाइप" in b and "हमारे" in b:
    b.remove("तिरछे")
    b.remove("टाइप")
    b.remove("हमारे")

# Print the modified list
print(" ".join(b))


# print(a)