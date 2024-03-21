
age = int(input("How old are you?: "))
if age == 100:
    print("Your are a century old")
elif age > 100:
    print("Your are olden than a century")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("Your haven't been born yet!")
else:
    print("Your are a child!")
