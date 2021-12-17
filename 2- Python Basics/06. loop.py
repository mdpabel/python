# for char in "Hello":
#     print(char)


# for num in range(2, 20, 2):
#     print(num)


names = ["zara", "mahadi"]

for name in names:
    if(name.startswith("v")):
        print("FOUND")
        break
else:
    print("NOT FOUND")


num = 0

while num != 5:
    num = int(input())
else:
    print("DONE!")
