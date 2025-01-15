import random

charecters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

num = int(input("Introdusca la cantidad de carecteres la contraseña debe de tener:"))

x = ""

for i in range(num):
    x += random.choice(charecters)

print("Su contraseña es:", x)
