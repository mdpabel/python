age = 19

if age > 18:
    print("Adult")
elif age > 13:
    print("Teenager")
else:
    print("Child")


# if age > 10 and age < 20:
#     print("Eligible")


if 10 < age < 20:
    print("Eligible")


res = "You are eligible" if 10 < age < 20 else "Your are not eligible"

print(res)
