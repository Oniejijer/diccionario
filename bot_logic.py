
import random


def gen_pass(pass_length):
    elements = "qwertyuiopasdfghjklzxcvbnm+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "HEADS"
    else:
        return "TAILS"
    
def info_1():
    print("COMANDOS DE BOT: Saludar = $hello, Despedir = $bye, Coin flip = $coin, Generar contraseña = $gen, Calculadora (solo sumar) = Cal ")
    

    
    
